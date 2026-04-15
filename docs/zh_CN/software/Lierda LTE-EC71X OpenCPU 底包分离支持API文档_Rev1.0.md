# Lierda LTE-EC71X OpenCPU 底包分离支持API文档\_Rev1.0

## 修订记录

| **文档版本** | **变更日期** | **修订人** | **审核人** | **变更内容** |
| --- | --- | --- | --- | --- |
| Rev1.0 | 26-03-13 | zlc |  | 新增文档 |

## 1 引言

本章节主要内容介绍Lierda LTE-EC71X OPENCPU 底包分离已经支持的利尔达自研功能API列表，其他平台支持不在该文档内说明，基于此文档，方便客户在进行功能开发时进行参考。

## 2 API 功能说明

### 2.1 基本信息 API

#### 2.1.1 Dev API 

| **函数** | **说明** |
| --- | --- |
| liot\_dev\_get\_imei() | 获取设备的 IMEI号 |
| liot\_dev\_get\_firmware\_version() | 获取设备的固件版本 |
| liot\_dev\_get\_sn() | 获取设备序列号 |
| liot\_dev\_get\_product\_id() | 获取设备制造商 ID |
| liot\_dev\_get\_firmware\_subversion() | 用于获取设备的子固件版本 |
| liot\_dev\_get\_model() | 获取设备型号 |
| liot\_dev\_set\_modem\_fun() | 设置设备 modem 功能 |
| liot\_dev\_get\_modem\_fun() | 获取设备 modem 功能 |
| liot\_dev\_memory\_size\_query() | 查询 heap 空间状态信息 |
| liot\_dev\_cfg\_wdt() | 配置看门狗（定时器）开关 |
| liot\_dev\_feed\_wdt() | 喂系统看门狗（将定时器清零） |
| Liot\_DevGetHardWareInfo() | 获取硬件型号 |
| Liot\_DevSetBandMode() | 设置可用频段 |
| Liot\_DevGetBandMode() | 查询可用频段与支持频段列表 |
| Liot\_DevFreqConfig() | 锁定频点、小区与清除优先频点 |
| Liot\_RRCRelease() | 使能快速释放 |
| Liot\_DevSetDnsServersAddr() | 设置主备DNS服务器地址 |
| Liot\_DevGetDnsServersAddr() | 查询主备DNS服务器地址 |

#### 2.1.2 datacall API

| **函数** | **说明** |
| --- | --- |
| liot\_network\_register\_cereg\_get() | 获取网络注册状态 |
| Liot\_DataCallCfgDefaultEpsBearer() | 设置或查询默认承载（CID 1）的 APN 和 IP 类型 |
| Liot\_PsEventCb() | 注册系统事件通知回调。 |

#### 2.1.3 SIM API

| **函数** | **说明** |
| --- | --- |
| liot\_sim\_get\_imsi() | 获取 SIM 卡的 IMSI |
| liot\_sim\_get\_iccid() | 获取 SIM 卡的 ICCID |
| liot\_sim\_get\_phonenumber() | 获取 SIM 卡本机号码 |
| liot\_sim\_get\_card\_status() | 获取 SIM 卡缓存状态信息 |

#### 2.1.4 NW API

| **函数** | **说明** |
| --- | --- |
| liot\_nw\_get\_csq() | 查询csq信号强度信息 |
| liot\_nw\_get\_operator\_name() | 获取当前注网的运营商信息 |
| liot\_nw\_get\_reg\_status () | 获取当前网络注册信息 |
| liot\_nw\_set\_selection () | 设置运营商 |
| liot\_nw\_get\_selection () | 获取选择的运营商信息 |
| liot\_nw\_get\_signal\_strength () | 获取详细信号强度信息 |
| liot\_nw\_get\_nitz\_time\_info () | 获取当前基站时间 |
| liot\_nw\_get\_cell\_info () | 获取当前服务及邻近小区信息 |
| liot\_nw\_register\_cb () | 注册事件回调函数 |
| liot\_nw\_get\_data\_count () | 获取上行和下行数据计数 |
| liot\_nw\_reset\_data\_count () | 重置上行和下行数据计数 |
| liot\_nw\_set\_ctzu\_switch() | 设置基站时间同步开关 |
| liot\_nw\_get\_ctzu\_switch() | 获取基站时间同步开关状态 |

#### 2.1.5 SMS API

| **函数** | **说明** |
| --- | --- |
| liot\_sms\_send\_msg() | 发送文本格式的短消息 |
| liot\_sms\_send\_pdu() | 发送PDU格式的短消息 |
| liot\_sms\_read\_msg\_list() | 获取短消息列表 |
| liot\_sms\_read\_msg\_ex() | 读取单条短消息 |
| liot\_sms\_delete\_msg\_ex() | 删除单条消息 |
| liot\_sms\_get\_center\_address() | 获取短消息中心号码 |
| liot\_sms\_set\_center\_address() | 设置短消息中心号码 |
| liot\_sms\_get\_storage\_info() | 获取SM与ME的存储信息 |
| liot\_sms\_set\_storage() | 设置短信存储位置 |
| liot\_sms\_get\_storage() | 获取短信存储位置 |

#### 2.1.6 Custom AT API

| **函数** | **说明** |
| --- | --- |
| liot\_open\_atcmd\_init() | 该函数用于AT功能的打开。 |
| liot\_atcmd\_register() | 该函数用于注册AT table表。 |
| liot\_atcmd\_reply() | 该指接口为AT的返回函数 |

### 2.2 Driver API列表

#### 2.2.1 OS API

##### 2.2.1.1 任务

| **函数** | **说明** |
| --- | --- |
| liot\_rtos\_task\_create() | 创建任务 |
| liot\_rtos\_task\_delete() | 删除任务 |
| liot\_rtos\_task\_yield() | 释放 CPU 使用权 |
| liot\_rtos\_task\_get\_current\_ref() | 获取当前任务的任务句柄 |
| liot\_rtos\_task\_change\_priority() | 切换任务优先级 |
| liot\_rtos\_task\_get\_status() | 获取任务状态信息 |
| liot\_rtos\_task\_sleep\_ms() | 设置任务休眠时间 |
| liot\_rtos\_task\_sleep\_s() | 设置任务休眠时间 |
| liot\_rtos\_task\_get\_stack\_space() | 获取任务堆栈空闲空间 |
| liot\_rtos\_task\_suspend() | 任务挂起 |
| liot\_rtos\_task\_resume() | 解除任务挂起，恢复为可调度的运行状态 |
| liot\_rtos\_get\_running\_time() | 获取 RTOS 系统的时钟节拍数转化的时间，单位ms |
| liot\_rtos\_get\_system\_tick() | 获取 RTOS 系统的时钟节拍数 |
| liot\_xPortGetTotalHeapSize() | 获取 FreeRTOS 堆的总大小 |
| liot\_xPortGetFreeHeapSize() | 获取 FreeRTOS 堆的空闲大小 |
| liot\_xPortGetMinimumEverFreeHeapSize() | 获取 FreeRTOS 堆在运行过程中最小空闲大小 |
| liot\_xPortGetMaximumFreeBlockSize() | 获取 FreeRTOS 最大可申请的内存块大小 |
| liot\_psram\_xPortGetTotalHeapSize() | 获取 PSRAM 的总大小 |
| liot\_psram\_xPortGetFreeHeapSize() | 获取 PSRAM 的空闲大小 |
| liot\_psram\_xPortGetMinimumEverFreeHeapSize() | 获取 PSRAM 在运行过程中最小空闲大小 |
| liot\_psram\_xPortGetMaximumFreeBlockSize() | 获取 PSRAM 在运行过程中最大可申请的内存块大小 |
| liot\_rtos\_is\_alive() | 判断任务是否处于运行态 |
| liot\_rtos\_task\_create\_static() | 静态方式创建任务 |

##### 2.2.1.2 临界区

| **函数** | **说明** |
| --- | --- |
| liot\_rtos\_enter\_critical() | 进入临界区 |
| liot\_rtos\_enter\_critical\_from\_isr() | 从中断中进入临界区 |
| liot\_rtos\_exit\_critical() | 退出临界区 |
| liot\_rtos\_exit\_critical\_from\_isr() | 从中断中退出临界区 |

##### 2.2.1.3 信号量

| **函数** | **说明** |
| --- | --- |
| liot\_rtos\_semaphore\_create() | 创建信号量 |
| liot\_rtos\_semaphore\_create\_ex() | 创建信号量 |
| liot\_rtos\_semaphore\_wait() | 设置信号量等待时间 |
| liot\_rtos\_semaphore\_release() | 释放信号量 |
| liot\_rtos\_semaphore\_get\_cnt() | 获取信号量值 |
| liot\_rtos\_semaphore\_delete() | 删除信号量 |

##### 2.2.1.4 互斥锁

| **函数** | **说明** |
| --- | --- |
| liot\_rtos\_mutex\_create() | 创建互斥锁 |
| liot\_rtos\_mutex\_lock() | 获取互斥锁，等待时间用户可以根据需求进行自定义 |
| liot\_rtos\_mutex\_try\_lock() | 尝试获得互斥锁，等待时间为永久等待 |
| liot\_rtos\_mutex\_unlock() | 释放互斥锁 |
| liot\_rtos\_mutex\_delete() | 删除互斥锁 |

##### 2.2.1.5 消息队列

| **函数** | **说明** |
| --- | --- |
| liot\_rtos\_queue\_create() | 创建消息队列 |
| liot\_rtos\_queue\_wait() | 等待队列中的消息 |
| liot\_rtos\_queue\_release() | 释放消息队列 |
| liot\_rtos\_queue\_get\_cnt() | 获取队列中的消息数量 |
| liot\_rtos\_queue\_delete() | 删除消息队列 |
| liot\_rtos\_queue\_reset() | 重置队列中的元素和更改队列长度 |
| liot\_rtos\_queue\_get\_space() | 查询队列中可用空间数量 |

##### 2.2.1.6 定时器

| **函数** | **说明** |
| --- | --- |
| liot\_rtos\_timer\_create() | 创建定时器 |
| liot\_rtos\_timer\_start() | 开启定时器 |
| liot\_rtos\_timer\_is\_running() | 判断定时器是否处于运行态 |
| liot\_rtos\_timer\_stop() | 停止定时器 |
| liot\_rtos\_timer\_delete() | 删除定时器 |
| ### liot\_rtos\_timer\_stop\_isr() | 在中断中停止定时器 |

##### 2.2.1.7 事件组

| **函数** | **说明** |
| --- | --- |
| liot\_rtos\_flag\_create | 创建事件组 |
| liot\_rtos\_flag\_get | 获取事件组当前的位状态 |
| liot\_rtos\_flag\_wait | 等待事件组的位满足指定的条件 |
| liot\_rtos\_flag\_release | 设置事件组中的事件位 |
| liot\_rtos\_flag\_clear | 清除事件组中的事件位 |
| liot\_rtos\_flag\_delete | 删除事件组 |

##### 2.2.1.8 PSRAM API

| **函数** | **说明** |
| --- | --- |
| liot\_rtos\_psram\_malloc | 从PSRAM申请内存。 |
| liot\_rtos\_psram\_free | 释放从PSRAM申请的内存。 |
| liot\_rtos\_psram\_realloc | 重新调整之前调用 liot\_rtos\_psram\_malloc所分配的 ptr 所指向的内存块的大小。 |
| liot\_psram\_xPortGetTotalHeapSize | 用于PSRAM总的HEAP大小。 |
| liot\_psram\_xPortGetFreeHeapSize | 用于获取PSRAM剩余可用内存大小。 |

##### 2.2.1.9 其他

| **函数** | **说明** |
| --- | --- |
| liot\_rtos\_malloc | 动态申请空间 |
| liot\_rtos\_calloc | 分配内存并初始化为 0 |
| liot\_rtos\_free | 释放动态申请空间 |
| liot\_rtos\_realloc | 重新分配内存 |
| liot\_true\_rand | 硬件随机数 |

#### 2.2.2 UART API

| **函数** | **说明** |
| --- | --- |
| Liot\_UartInit | Uart 初始化接口 |
| Liot\_UartDeinit | Uart 去初始化接口 |
| Liot\_UartSend | Uart 发送接口 |

#### 2.2.3 USB API

| **函数** | **说明** |
| --- | --- |
| liot\_usb\_bind\_hotplug\_cb | 注册 USB 事件回调函数 |
| liot\_usb\_get\_hotplug\_state | 获取 USB 插拔状态 |
| liot\_usb\_drv\_is\_enabled | 获取 USB 初始化状态 |
| liot\_usb\_drv\_enable | 初始化 USB 驱动 |
| liot\_usb\_drv\_disable | 去初始化 USB 驱动 |

#### 2.2.4 ADC API

| **函数** | **说明** |
| --- | --- |
| liot\_adc\_get\_volt\_raw | 读取 ADC 通道中的模拟电压值源数据 |

#### 2.2.5 GPIO API

| **函数** | **说明** |
| --- | --- |
| Liot\_GpioInit | GPIO 初始化接口 |
| Liot\_GpioGetLevel | GPIO 去初始化接口。 |
| Liot\_GpioSetLevel | GPIO 设置电平 |
| Liot\_GpioIntEnable | 使能普通 gpio 中断源 |
| Liot\_GpioIntDisable | 关闭普通 gpio 中断源 |
| Liot\_AonPowerCtl | 控制 AGPIO 电源域开关 |
| Liot\_SetVoltage | 设置电源域电压 |
| Liot\_SetPinFunc | 设置模组引脚复用功能 |
| Liot\_GetPinFunc | 获取模组引脚复用功能 |
| Liot\_WakeupIntInit | 初始化 wakeup 引脚中断 |
| Liot\_WakeupIntDeinit | 去初始化 wakeup 引脚中断 |
| Liot\_WakeupPadGetLevel | 获取wakeup 引脚电平 |

#### 2.2.6 PWM API

| **函数** | **说明** |
| --- | --- |
| liot\_pwm\_open() | 打开 PWM 功能 |
| liot\_pwm\_close() | 关闭 PWM 功能 |
| liot\_pwm\_enable() | 使能 PWM 并配置 PWM 的脉冲周期和占空比 |
| liot\_pwm\_disable() | 暂停 PWM 功能 |
| liot\_pwm\_set\_duty\_cycle() | 设置PWM占空比 |

#### 2.2.7 APWM API

| **函数** | **说明** |
| --- | --- |
| Liot\_ApwmCfg() | 打开 PWM 功能 |
| Liot\_ApwmEnable() | 关闭 PWM 功能 |

#### 2.2.8 I2C API

| **函数** | **说明** |
| --- | --- |
| liot\_I2cInit() | 初始化 I2C 总线。 |
| liot\_I2cRelease() | 释放 I2C 总线。 |
| liot\_I2cWrite() | 向 I2C 总线写入数据，从设备的寄存器地址长度为 8 位。 |
| liot\_I2cRead() | 从 I2C 总线读取数据，从设备的寄存器地址长度为 8 位。 |
| liot\_I2cWrite\_16bit\_addr() | 向 I2C 总线写入数据，从设备的寄存器地址长度为 16 位。 |
| liot\_I2cRead\_16bit\_addr() | 从 I2C 总线读取数据，从设备的寄存器地址长度为 16 位。 |

#### 2.2.9 FLASH API

| **函数** | **说明** |
| --- | --- |
| liot\_flash\_erase() | 擦除 flash 中的数据。 |
| liot\_flash\_read() | 从 flash 中读取数据。 |
| liot\_flash\_write() | 向 flash 中写入数据。 |

#### 2.2.10 RTC API

| **函数** | **说明** |
| --- | --- |
| liot\_rtc\_set\_time() | 设置rtc时间 |
| liot\_rtc\_get\_time() | 获取rtc时间 |
| liot\_rtc\_get\_time\_s() | 获取rtc时间转换成秒数 |
| liot\_rtc\_get\_localtime() | 获取本地rtc时间 |
| liot\_rtc\_set\_timezone() | 设置时区，以15分钟为单位 |
| liot\_rtc\_get\_timezone() | 获取时区，以15分钟为单位 |
| liot\_rtc\_print\_time() | 打印rtc时间 |
| liot\_rtc\_set\_alarm() | 设置rtc alarm时间 |
| liot\_rtc\_get\_alarm() | 获取rtc alarm时间 |
| liot\_rtc\_enable\_alarm() | 打开和关闭rtc alarm |
| liot\_rtc\_register\_cb() | 注册rtc alarm 回调函数 |
| Liot\_GetTimestamp() | 获取rtc时间转换成毫秒数 |

#### 2.2.11 FS API

| **函数** | **说明** |
| --- | --- |
| liot\_fopen() | 根据文件路径或文件名打开一个文件。 |
| liot\_fclose() | 关闭一个已打开的文件。 |
| liot\_remove() | 删除一个文件。 |
| liot\_fread() | 读取文件内容。 |
| liot\_fwrite() | 向文件写入内容。 |
| liot\_fseek() | 设置文件指针位置。 |
| liot\_frewind() | 将文件位置指针设置到文件的开头。 |
| liot\_ftell() | 从文件指针位置截断数据。 |
| liot\_fstat() | 根据文件描述符获取文件的状态。 |
| liot\_stat() | 根据文件名获取文件信息。 |
| liot\_ftruncate() | 将文件从指定长度截断。 |
| liot\_fsize() | 获取文件大小。 |
| liot\_file\_exist() | 根据文件名判断文件是否存在。 |
| liot\_mkdir() | 创建一个文件夹。 |
| liot\_opendir() | 打开一个文件夹。 |
| liot\_closedir() | 关闭一个已打开的文件夹。 |
| liot\_readdir() | 获取文件夹信息。 |
| liot\_rename() | 更改文件夹命名。 |
| liot\_fsync() | 同步文件数据。 |
| liot\_internal\_fs\_free\_size\_get() | 获取文件系统剩余大小。 |

#### 2.2.12 NV API

| **函数** | **说明** |
| --- | --- |
| liot\_nvm\_fwrite() | 写入简单配置文件 |
| liot\_nvm\_fread() | 读取简单配置文件 |
| liot\_cust\_nvm\_fwrite() | 写入用户自定义简单配置文件 |
| liot\_cust\_nvm\_fread() | 读取用户自定义简单配置文件 |

#### 2.2.13 低功耗相关

| **函数** | **说明** |
| --- | --- |
| Liot\_SleepSetMode() | 设置功耗模式 |
| Liot\_SleepTimerStart() | 开启低功耗定时器 |
| Liot\_SleepTimerStop() | 停止低功耗定时器 |
| Liot\_SleepTimerCheck() | 检测低功耗定时器是否在运行 |
| Liot\_SleepTimerGetID() | 获取唤醒系统的低功耗ID |

#### 2.2.14 PowerKey API

| **函数** | **说明** |
| --- | --- |
| liot\_power\_down() | 模组关机 |
| liot\_power\_reset() | 模组复位 |
| liot\_get\_pwrkey\_status() | 获取pwrkey电平状态 |
| liot\_pwrkey\_callback\_register() | 注册pwrkey中断回调 |
| liot\_pwrkey\_shutdown\_time\_set() | 设置pwrkey关机超时时间 |
| liot\_get\_powerup\_reason() | 获取复位原因 |
| liot\_set\_pwrkey\_pull() | 设置pwrkey上下拉 |
| liot\_set\_pwrkey\_Init() | 设置pwrkey初始化状态 |

#### 2.2.15 GNSS API

| **函数** | **说明** |
| --- | --- |
| liot\_gnss\_config() | 配置gnss模块参数 |
| liot\_agnss\_config() | 配置agnss功能参数 |
| liot\_gnss\_open() | 开启gnss模块 |
| liot\_gnss\_close() | 关闭gnss模块 |
| liot\_gnss\_get\_location() | 获取定位信息 |
| liot\_gnss\_get\_nmea() | 获取指令NMEA语句 |
| liot\_gnss\_close\_backup\_power() | 关闭GNSS芯片备用电源 |

#### 2.2.16 SPI API

| liot\_spi\_init() | 该函数用于初始化 SPI |
| --- | --- |
| liot\_spi\_init\_ext() | 该函数用于初始化 SPI（配置 SPI 总线参数） |
| liot\_spi\_write\_read() | 该函数用于设置通过 SPI 同时发送和接收数据 |
| liot\_spi\_read() | 该函数用于设置通过 SPI 接收数据 |
| liot\_spi\_write() | 该函数用于设置通过 SPI 发送数据 |
| liot\_spi\_release() | 该函数用于释放 SPI 总线 |

### 2.3 应用协议 API

#### 2.3.1 HTTP API

| **函数** | **说明** |
| --- | --- |
| liot\_httpc\_new() | 创建一个新的HTTP客户端句柄并初始化HTTP客户端资源 |
| liot\_httpc\_perform() | 发送 HTTP 请求 |
| liot\_httpc\_stop() | 停止HTTP请求 |
| liot\_httpc\_release() | 释放 HTTP 客户端资源 |
| liot\_httpc\_setopt() | 配置 HTTP 客户端属性 |
| liot\_httpc\_getinfo() | 获取HTTP消息头信息 |
| liot\_httpc\_formadd() | 配置 HTTP 表单属性。 |
| liot\_httpc\_is\_running() | 判断HTTP客户端是否处于运行态 |
| liot\_httpc\_url\_parse() | 解析URL |

#### 2.3.2 SSL API

| **函数** | **说明** |
| --- | --- |
| Liot\_SSLSetCfg() | 配置SSL相关参数配置 |
| Liot\_SSLSocketOpen() | 创建SSL连接 |
| Liot\_SSLSocketSend() | 发送数据 |
| Liot\_SSLSocketGetStatus() | 查询SSL连接状态 |
| Liot\_SSLSocketClose() | 关闭SSL连接 |

#### 2.3.3 MQTT API

| **函数** | **说明** |
| --- | --- |
| liot\_mqtt\_client\_init\_ex() | 初始化 MQTT 客户端资源并创建一个新的 MQTT 客户端句柄 |
| liot\_mqtt\_connect() | 配置 MQTT 上下文，并与服务器建立连接 |
| liot\_mqtt\_publish() | 向指定topic发布消息 |
| liot\_mqtt\_sub\_unsub() | 订阅/取消订阅topic |
| liot\_mqtt\_disconnect() | 断开连接 |
| liot\_mqtt\_set\_inpub\_callback() | 设置接收服务器发布消息的处理回调函数 |
| liot\_mqtt\_client\_is\_connected() | 查询mqtt连接状态 |
| liot\_mqtt\_client\_deinit() | 释放mqtt客户端资源 |
| liot\_mqtt\_pingreq() | 发送ping消息 |
| liot\_onenet\_generate\_auth\_token() | 获取onenet平台token |

#### 2.3.4 FTP API

| **函数** | **说明** |
| --- | --- |
| liot\_ftp\_client\_new() | 创建FTP客户端 |
| liot\_ftp\_client\_release() | 释放FTP客户端 |
| liot\_ftp\_client\_setopt() | 设置客户端选项 |
| liot\_ftp\_client\_open() | 连接FTP服务器 |
| liot\_ftp\_client\_close() | 断开FTP服务器 |
| liot\_ftp\_client\_get\_ex() | 下载文件 |
| liot\_ftp\_client\_put\_ex() | 上传文件 |
| liot\_ftp\_client\_delete() | 删除文件 |
| liot\_ftp\_client\_pwd() | 获取当前目录路径 |
| liot\_ftp\_client\_cwd() | 变更当前目录路径 |
| liot\_ftp\_client\_mkdir() | 新建目录 |
| liot\_ftp\_client\_rmdir() | 删除目录 |
| liot\_ftp\_client\_list() | 获取目录信息 |
| liot\_ftp\_client\_size() | 获取文件大小 |
| liot\_ftp\_client\_rename() | 重命名文件 |
| liot\_ftp\_client\_FileTpye() | 设置传输文件类型 |

#### 2.3.5 NTP API

| **函数** | **说明** |
| --- | --- |
| liot\_ntp\_sync() | 打开 NTP 同步时间的功能 |

#### 2.3.6 PING API

| **函数** | **说明** |
| --- | --- |
| liot\_ping\_start() | 启用ping功能 |

#### 2.3.7 LBS API

| **函数** | **说明** |
| --- | --- |
| liot\_lbs\_get\_position() | 该函数用于请求获取定位信息。 |

#### 2.3.8 WifiScan API

| **函数** | **说明** |
| --- | --- |
| liot\_wifiscan\_open() | 启用 Wi-Fi Scan |
| liot\_wifiscan\_close() | 禁用 Wi-Fi Scan |
| liot\_wifiscan\_option\_set() | 配置 Wi-Fi Scan 扫描参数 |
| liot\_wifiscan\_do() | 进行 Wi-Fi Scan 同步模式扫描 |
| liot\_wifiscan\_register\_cb() | 开始 Wi-Fi Scan 异步模式扫描 |
| liot\_wifiscan\_async() | 注册回调函数 |

#### 2.3.9 FOTA API

| **函数** | **说明** |
| --- | --- |
| Liot\_FotaUpgrade() | 查分升级模组接口 |
| liot\_fota\_image\_verify() | 用于校验文件系统中存储的升级包信息，校验后写入fota分区 |
| liot\_fota\_clear() | 用于初始化并清空模块升级区域 |
| liot\_fota\_get\_result() | 用于获取 FOTA 升级结果 |
| liot\_fota\_power\_reset() | 用于重启模块 |
| liot\_fota\_nvm\_init() | 用于初始化并清空模块升级fota分区 |
| liot\_fota\_nvm\_write() | 用于将模块文件直接写入fota分区 |
| liot\_fota\_nvm\_free\_size\_get() | 用于获取fota分区大小 |
| liot\_fota\_nvm\_image\_verify() | 用于校验fota分区中存储的升级包信息 |

#### 2.3.10 APP OTA API

| **函数** | **说明** |
| --- | --- |
| Liot\_FotaAppUpgradeCheck() | 全量升级APP分区升级包检测接口 |

### 2.4 多媒体 API

#### 2.4.1 AUDIO API

| **函数** | **说明** |
| --- | --- |
| Liot\_SoundInit() | 音频初始化接口 |
| Liot\_SoundDeInit() | 音频去初始化接口。 |
| Liot\_SoundSetVolume() | 设置音量大小 |
| Liot\_SoundGetVolume() | 获取音量大小 |
| Liot\_SoundSetMicVolume() | 设置麦克风音量 |
| Liot\_SoundPlay() | 播放音频 |
| Liot\_SoundRecord() | 录制音频 |
| Liot\_SoundPlayPause() | 播放暂停 |
| Liot\_SoundPlayResume() | 播放恢复 |
| Liot\_SoundPlayMp3File() | 播放 MP3 文件 |

#### 2.4.2 TTS API \*

| **函数** | **说明** |
| --- | --- |
| liot\_tts\_engine\_init() | 初始化 TTS 引擎 |
| liot\_tts\_set\_config\_param() | 播放 TTS 前设置配置选项 |
| liot\_tts\_get\_config\_param() | 获取 TTS 的配置选项 |
| liot\_tts\_start() | 开始播放TTS |
| liot\_tts\_end() | TTS 播放完成时释放占用资源 |
| liot\_tts\_exit() | 中断 TTS 播放并退出 TTS |
| liot\_tts\_is\_running() | 返回TTS运行状态 |
| liot\_tts\_set\_resource() | 设定TTS资源 |
| liot\_utf8\_to\_gbk\_str() | 将utf8编码字符串转成gbk编码字符串 |

#### 2.4.3 LCD API

| **函数** | **说明** |
| --- | --- |
| liot\_lcd\_init() | LCD初始化 |
| liot\_lcd\_clear\_screen() | LCD全屏刷新 |
| liot\_lcd\_draw\_point() | LCD画点 |
| liot\_lcd\_draw\_line() | LCD画线 |
| liot\_lcd\_draw\_rectangle() | LCD画矩形 |
| liot\_lcd\_draw\_circle() | LCD画圆 |
| liot\_lcd\_write() | LCD显示图片 |
| liot\_lcd\_set\_brightness() | LCD设置亮度 |
| liot\_lcd\_display\_on() | LCD开启显示 |
| liot\_lcd\_display\_off() | LCD关闭显示 |
| liot\_lcd\_sleep\_in() | LCD进入休眠 |
| liot\_lcd\_sleep\_out() | LCD退出休眠 |

#### 2.4.4 KeyPad API

| **函数** | **说明** |
| --- | --- |
| liot\_keypad\_init() | 初始化矩阵键盘 |
| liot\_keypad\_state() | 获取矩阵键盘状态 |

#### 2.4.5 Camera API

| **函数** | **说明** |
| --- | --- |
| liot\_CamInit () | 初始化摄像头功能 |
| liot\_CamDeInit () | 关闭摄像头功能 |
| liot\_CamCaptureImage () | 获取一张图片 |
| liot\_CamPreview () | 打开摄像头在LCD屏幕上预览（暂不支持） |
| liot\_CamStopPreview () | 打开摄像头在LCD屏幕上预览（暂不支持） |

#### 2.4.6 Decode API

| **函数** | **说明** |
| --- | --- |
| liot\_decoder\_set\_auth\_key() | 设置解码库认证密钥 |
| liot\_get\_decoder\_version() | 获取解码库版本信息 |
| liot\_decoder\_init() | 初始化解码库 |
| liot\_destroy\_decoder() | 关闭解码库 |
| liot\_image\_decoder() | 解码照片 |
| liot\_get\_decoder\_result() | 获取解码结果 |

#### 2.4.7 Volte API

| **函数** | **说明** |
| --- | --- |
| liot\_volte\_ims\_reg\_set() | IMS注册状态上报 |
| liot\_volte\_ims\_reg\_get() | IMS注册状态获取 |
| liot\_volte\_vdp\_set() | 设置语音域选项 |
| liot\_volte\_vdp\_get() | 获取语音域选项 |
| liot\_volte\_usage\_set() | 设置模块用途 |
| liot\_volte\_usage\_get() | 获取模块用途 |
| liot\_volte\_codec\_type\_set() | 设置codec类型 |
| liot\_voice\_auto\_answer() | 设置自动接听 |
| liot\_voice\_call\_start() | 拨打电话 |
| liot\_voice\_call\_answer() | 接听电话 |
| liot\_voice\_call\_end() | 挂断电话 |
| liot\_voice\_call\_start\_dtmf() | 发送DTMF |
| liot\_voice\_call\_clcc() | 获取当前电话列表 |
| liot\_voice\_get\_phone\_num() | 获取当前电话号码 |
| liot\_voice\_call\_callback\_register() | 注册回调函数 |