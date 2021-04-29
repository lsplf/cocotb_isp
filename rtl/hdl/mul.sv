module mul (
    input                       clk,
    input                       rst,
    input           [ 7 : 0]    a,
    input           [ 7 : 0]    b,
    output  logic   [15 : 0]    p
);

    always @(posedge clk) begin
        if(rst) begin
            p <= 16'd0;
        end
        else begin
            p<= a * b;
        end
    end
    
endmodule