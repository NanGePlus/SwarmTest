# 1、项目介绍
## 1.1、本次分享介绍                      
(1)Swarm核心概念介绍                                                           
(2)相关案例测试Swarm核心功能                                 

## 1.2 Swarm介绍
Swarm目前是一个实验性的样本框架，不打算用于生产，因此没有官方支持              
Swarm的诞生是基于Routines和Handoffs的概念验证，最后将这些想法打包成了一个名为Swarm的示例库            
Swarm探索的是轻量级、可控性、可拓展性和高度定制化的设计模式，适用于处理需要大量独立功能和指令的场景                           
github地址:https://github.com/openai/swarm/tree/main                 
### (1)核心概念
核心概念相关文档地址:https://cookbook.openai.com/examples/orchestrating_agents                                    
**Routines**          
其概念官方并没有给出严格的定义                        
具体来说，Routines可以理解为一系列自然语言指令以及完成这些指令所需要的工具         
即一组步骤和执行这些步骤的工具           
**Handoffs**              
定义为一个AgentA将正在进行的对话移交给另一AgentB           
在这种情况下，AgentB完全了解之前的对话内容                            
### (2)核心流程
从当前Agent获取完成信息->执行工具调用并追加结果->必要时移交Agent->必要时更新上下文变量->若无新函数调用则返回                     
### (3)Agent核心功能      
**name**                   
指定Agent的名称，默认值为“Agent”             
**model**                  
指定Agent使用的大语言模型，默认值为“gpt-4o”                   
**instructions**            
Agent指令，在使用时会被处理为系统提示词                                
任何时候，只有激活该Agent，指令才会生效(若有Agent切换时，系统提示词会变，但会话记录不会变)                  
指令可以是普通的字符串，也可以是返回字符串的函数                   
函数可以选择接收一个context_variables参数，该参数由传入的client.run()的context_variables参数填充                                    
**Functions**        
提供给Agent使用的工具集合          
函数支持返回字符串                   
函数支持返回一个Agent，响应的动作处理则为将当前对话移交至该Agent                  
若函数定义了context_variables参数，它将由传入的client.run()的context_variables参数填充                 
若调用函数时出错(函数丢失、参数错误等)对话会附加错误响应，以便Agent恢复                              
若调用多个函数，它们将按照顺序执行                               
移交和更新上下文变量，一个Agent可通过在函数中以返回的方式移交给另一个Agent                      
支持通过返回一个更完整的结果对象来返回:一个值、更新Agent、更新上下文变量，或者三者的合集            


# 2、前期准备工作
## 2.1 开发环境搭建:anaconda、pycharm
anaconda:提供python虚拟环境，官网下载对应系统版本的安装包安装即可                                      
pycharm:提供集成开发环境，官网下载社区版本安装包安装即可                                               
可参考如下视频进行安装，【大模型应用开发基础】集成开发环境搭建Anaconda+PyCharm                                                          
https://www.bilibili.com/video/BV1q9HxeEEtT/?vd_source=30acb5331e4f5739ebbad50f7cc6b949                             
https://youtu.be/myVgyitFzrA          

## 2.2 大模型相关配置
(1)GPT大模型使用方案              
(2)非GPT大模型(国产大模型)使用方案(OneAPI安装、部署、创建渠道和令牌)                 
(3)本地开源大模型使用方案(Ollama安装、启动、下载大模型)                         
可参考如下视频:                         
提供一种LLM集成解决方案，一份代码支持快速同时支持gpt大模型、国产大模型(通义千问、文心一言、百度千帆、讯飞星火等)、本地开源大模型(Ollama)                       
https://www.bilibili.com/video/BV12PCmYZEDt/?vd_source=30acb5331e4f5739ebbad50f7cc6b949                 
https://youtu.be/CgZsdK43tcY           


# 3、项目初始化
## 3.1 下载源码
GitHub或Gitee中下载工程文件到本地，下载地址如下：                
https://github.com/NanGePlus/SwarmTest                                                               
https://gitee.com/NanGePlus/SwarmTest                                    

## 3.2 构建项目
使用pycharm构建一个项目，为项目配置虚拟python环境               
项目名称：SwarmTest                                                 

## 3.3 将相关代码拷贝到项目工程中           
直接将下载的文件夹中的文件拷贝到新建的项目目录中               

## 3.4 安装项目依赖          
命令行终端中执行如下命令安装依赖包            
pip install git+https://github.com/openai/swarm.git                    
或者将源码下载后通过如下方式进行安装                
cd swarm                          
pip install .                       
                

# 4、测试
相关测试代码在nangeAGICode文件夹下               


   






















