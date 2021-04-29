### Cocotb 示例工程
---
#### 目录结构
**rtl**：hdl放用户编辑的hdl文件，ip放ip核  
**model**：放python编写的算法模型文件  
**test**:  test_mult为cocotb测试平台, Makefile为执行脚本
**build**: 放波形文件

#### 使用方法
1. 打开命令行，cd test, 然后执行make clean清理原有运行结果
1. 打开命令行，cd test, 然后执行make
2. 然后再打开命令行，执行gtkwave build/xxx.vcd, 查看波形
   
#### 注意事项
1. python模块调用，如果不在当前目录下的包，需要在引用时添加  
   如下代码：  
   ```python
    import sys,os  
    sys.path.append(os.path.dirname(__file__) + os.sep + '../')  
    from model import xxx_model  
   ```  
2. 一般在需要再额外建立一个xxx_wrapper.sv，用来例化需要被仿真的模块，  
   且在这个模块里面添加如下代码，用来dump波形。
   ```verilog
    initial begin
        $dumpfile("xxx.vcd");
        $dumpvars();
    end
   ```  
3. gtkwave打开一次波形文件后，后面再次仿真，可以直接点击界面上  
   的reload,不用重新打开vcd文件。  
   
   

