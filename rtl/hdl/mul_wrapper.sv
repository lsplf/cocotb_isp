
module mul_wrapper (
    input                       clk,
    input                       rst,
    input           [ 7 : 0]    a,
    input           [ 7 : 0]    b,
    output  logic   [15 : 0]    p
);

    mul  u_mul (
        .clk   ( clk  ),
        .rst   ( rst  ),
        .a     ( a    ),
        .b     ( b    ),

        .p     ( p    )
    );

     initial begin
        $dumpfile("build/mul.vcd");
        $dumpvars();
 end

endmodule