> 本文由 [简悦 SimpRead](http://ksria.com/simpread/) 转码， 原文地址 [blog.csdn.net](https://blog.csdn.net/chushoufengli/article/details/79840935)

**rm(remove) 指令用于删除目录或文件：**  
语法：           rm [-dfirv][--help][--version][文件或目录...]  
补充说明：    执行 rm 指令可删除文件或目录，如欲删除目录必须加上参数”-r”，否则预设仅会删除文件。   
参数：  
                     -d 或–directory 　直接把欲删除的目录的硬连接数据删成 0，删除该目录。   
                     -f 或–force 　强制删除文件或目录。   
                     -i 或–interactive 　删除既有文件或目录之前先询问用户。   
                     -r 或 - R 或–recursive 　递归处理，将指定目录下的所有文件及子目录一并处理。   
                     -v 或–verbose 　显示指令执行过程。

**例如：**

删除文件夹：

                     rm -rf code

                     将会删除 code 目录以及其下所有文件、文件夹。（注意一定要加 -r，不然很麻烦）

删除文件：

                     rm -f  001.cpp