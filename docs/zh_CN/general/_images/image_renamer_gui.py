import re
import shutil
import uuid
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox


IMAGE_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".bmp",
    ".gif",
    ".webp",
    ".tif",
    ".tiff",
}

MARKDOWN_IMAGE_PATTERN = re.compile(r"!\[[^\]]+\.png\]\((.*?)\)", re.IGNORECASE)


def natural_sort_key(text: str):
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r"(\d+)", text)]


def get_image_files(folder: Path):
    return sorted(
        [item for item in folder.iterdir() if item.is_file() and item.suffix.lower() in IMAGE_EXTENSIONS],
        key=lambda item: natural_sort_key(item.name),
    )


def build_target_names(image_files, base_name: str):
    return [f"{base_name}{index}{image.suffix.lower()}" for index, image in enumerate(image_files, start=1)]


def rename_images(folder: Path, image_files, target_names):
    temp_records = []
    for source in image_files:
        temp_name = f"__renaming__{uuid.uuid4().hex}{source.suffix.lower()}"
        temp_path = folder / temp_name
        source.rename(temp_path)
        temp_records.append((source, temp_path))

    renamed_paths = []
    try:
        for target_name, (_, temp_path) in zip(target_names, temp_records):
            target_path = folder / target_name
            if target_path.exists():
                raise ValueError(f"目标文件已存在：{target_name}")
            temp_path.rename(target_path)
            renamed_paths.append(target_path)
    except Exception:
        for original_path, temp_path in temp_records:
            if temp_path.exists():
                temp_path.rename(original_path)
        raise

    return renamed_paths


def replace_markdown_images(content: str, renamed_paths, replace_count: int):
    renamed_names = [path.name for path in renamed_paths]
    index = 0

    def replacer(match):
        nonlocal index
        if index >= replace_count:
            return match.group(0)
        new_name = renamed_names[index]
        index += 1
        return f"![]({new_name})"

    updated_content = MARKDOWN_IMAGE_PATTERN.sub(replacer, content)
    return updated_content, index


def process_images_and_markdown(folder_path: str, base_name: str, markdown_path: str, force_replace: bool):
    folder = Path(folder_path).expanduser().resolve()
    markdown_file = Path(markdown_path).expanduser().resolve()

    if not folder.exists() or not folder.is_dir():
        raise ValueError("路径不存在，或不是有效文件夹。")
    if not base_name.strip():
        raise ValueError("名称不能为空。")
    if not markdown_file.exists() or not markdown_file.is_file() or markdown_file.suffix.lower() != ".md":
        raise ValueError("请导入有效的 .md 文档。")

    image_files = get_image_files(folder)
    if not image_files:
        raise ValueError("该路径下没有找到支持的图片文件。")

    markdown_content = markdown_file.read_text(encoding="utf-8")
    matches = list(MARKDOWN_IMAGE_PATTERN.finditer(markdown_content))
    if not matches:
        raise ValueError("Markdown 中没有找到符合规则的图片标记，格式应为 ![任意名称.png](xxx)。")

    image_count = len(image_files)
    markdown_count = len(matches)
    if image_count != markdown_count and not force_replace:
        raise RuntimeError(f"COUNT_MISMATCH:{image_count}:{markdown_count}")

    replace_count = min(image_count, markdown_count)
    if replace_count == 0:
        raise ValueError("没有可处理的图片或 Markdown 图片标记。")

    target_names = build_target_names(image_files, base_name)
    renamed_paths = rename_images(folder, image_files, target_names)

    backup_path = markdown_file.with_suffix(markdown_file.suffix + ".bak")
    shutil.copy2(markdown_file, backup_path)

    try:
        updated_content, replaced_count = replace_markdown_images(markdown_content, renamed_paths, replace_count)
        markdown_file.write_text(updated_content, encoding="utf-8")
    except Exception:
        if backup_path.exists():
            shutil.copy2(backup_path, markdown_file)
        raise

    return {
        "image_count": image_count,
        "markdown_count": markdown_count,
        "replaced_count": replaced_count,
        "renamed_names": [path.name for path in renamed_paths],
        "backup_path": str(backup_path),
        "markdown_path": str(markdown_file),
    }


class ImageRenamerApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("图片与 Markdown 批量处理")
        self.root.geometry("760x430")
        self.root.resizable(False, False)

        self.path_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.doc_var = tk.StringVar()
        self.status_var = tk.StringVar(value="请选择图片路径并导入 Markdown 文档。")

        self.build_ui()

    def build_ui(self):
        container = tk.Frame(self.root, padx=20, pady=20)
        container.pack(fill="both", expand=True)

        tk.Label(container, text="输入框1：图片路径", anchor="w").grid(row=0, column=0, sticky="w")
        tk.Entry(container, textvariable=self.path_var, width=72).grid(row=1, column=0, padx=(0, 10), sticky="we")
        tk.Button(container, text="选择路径", command=self.choose_folder, width=12).grid(row=1, column=1, sticky="e")

        tk.Label(container, text="输入框2：图片名称前缀", anchor="w").grid(row=2, column=0, pady=(16, 0), sticky="w")
        tk.Entry(container, textvariable=self.name_var, width=72).grid(row=3, column=0, columnspan=2, sticky="we")

        tk.Label(container, text="导入 Markdown 文档", anchor="w").grid(row=4, column=0, pady=(16, 0), sticky="w")
        tk.Entry(container, textvariable=self.doc_var, width=72).grid(row=5, column=0, padx=(0, 10), sticky="we")
        tk.Button(container, text="导入文档", command=self.choose_markdown, width=12).grid(row=5, column=1, sticky="e")

        tk.Button(container, text="处理图片", command=self.handle_process, height=2).grid(
            row=6, column=0, columnspan=2, pady=22, sticky="we"
        )

        tk.Label(
            container,
            text=(
                "处理规则：\n"
                "1. 按文件名自然排序重命名图片，例如 名称1.png、名称2.jpg\n"
                "2. 从上到下扫描 Markdown 中 [] 内为 .png 文件名的图片标记\n"
                "3. 依次替换为重命名后的图片名，格式改为 ![](新图片名)\n"
                "4. 修改 Markdown 前会自动生成同目录备份文件 .md.bak"
            ),
            justify="left",
            fg="#444444",
        ).grid(row=7, column=0, columnspan=2, sticky="w")

        tk.Label(container, textvariable=self.status_var, anchor="w", fg="#006400", justify="left").grid(
            row=8, column=0, columnspan=2, pady=(18, 0), sticky="w"
        )

        container.grid_columnconfigure(0, weight=1)

    def choose_folder(self):
        folder = filedialog.askdirectory(title="选择图片所在文件夹")
        if folder:
            self.path_var.set(folder)
            self.status_var.set("已选择图片路径。")

    def choose_markdown(self):
        file_path = filedialog.askopenfilename(
            title="选择 Markdown 文档",
            filetypes=[("Markdown Files", "*.md")],
        )
        if file_path:
            self.doc_var.set(file_path)
            self.status_var.set("Markdown 文档已导入。")

    def handle_process(self):
        folder_path = self.path_var.get().strip()
        base_name = self.name_var.get().strip()
        markdown_path = self.doc_var.get().strip()

        try:
            result = process_images_and_markdown(folder_path, base_name, markdown_path, force_replace=False)
        except RuntimeError as exc:
            message = str(exc)
            if message.startswith("COUNT_MISMATCH:"):
                _, image_count, markdown_count = message.split(":")
                should_continue = messagebox.askyesno(
                    "数量不一致",
                    (
                        f"图片数量：{image_count}\n"
                        f"Markdown 待替换数量：{markdown_count}\n\n"
                        "数量不一致，说明内容可能有问题。\n"
                        "是否仍继续处理？\n"
                        "继续后只会按较小数量进行替换。"
                    ),
                )
                if not should_continue:
                    self.status_var.set("已取消处理，等待用户确认后再执行。")
                    return

                try:
                    result = process_images_and_markdown(folder_path, base_name, markdown_path, force_replace=True)
                except Exception as inner_exc:
                    self.status_var.set("处理失败。")
                    messagebox.showerror("错误", str(inner_exc))
                    return
            else:
                self.status_var.set("处理失败。")
                messagebox.showerror("错误", message)
                return
        except Exception as exc:
            self.status_var.set("处理失败。")
            messagebox.showerror("错误", str(exc))
            return

        self.status_var.set(
            f"处理完成：重命名 {result['image_count']} 张图片，替换 {result['replaced_count']} 处 Markdown 图片标记。"
        )

        preview = "\n".join(result["renamed_names"][:10])
        if len(result["renamed_names"]) > 10:
            preview += "\n..."

        messagebox.showinfo(
            "处理完成",
            (
                f"图片数量：{result['image_count']}\n"
                f"Markdown 图片标记数量：{result['markdown_count']}\n"
                f"实际替换数量：{result['replaced_count']}\n\n"
                f"已备份文档：{result['backup_path']}\n\n"
                f"前 10 个重命名结果：\n{preview}"
            ),
        )


def main():
    root = tk.Tk()
    app = ImageRenamerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
