modbus

```python
import modbus_tk.modbus_tcp as mt
import modbus_tk.defines as md
# 远程连接到服务器端
master = mt.TcpMaster("192.168.1.10", 502)
master.set_timeout(5.0)
# @slave=1 : identifier of the slave. from 1 to 247. 0为广播所有的slave
# @function_code=READ_HOLDING_REGISTERS：功能码
# @starting_address=1：开始地址,寄存器起始地址，从0开始
# @quantity_of_x=3：寄存器/线圈的数量,寄存器连续个数
# @output_value：一个整数或可迭代的值：1/[1,1,1,0,0,1]/xrange(12),写命令时的数值
#Scan Rate：读取数据的周期，程序中体现为执行 execute()方法的周期
# @data_format
# @expected_length
Hold_value = master.execute(slave=1, function_code=md.READ_HOLDING_REGISTERS, starting_address=1, quantity_of_x=3, output_value=5)
Coils_value = master.execute(slave=1, function_code=md.READ_COILS, starting_address=1, quantity_of_x=3, output_value=5)
print(Hold_value) # 取到的寄存器的值格式为元组(55, 12, 44)
```

