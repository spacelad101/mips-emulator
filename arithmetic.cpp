#include <iostream>
#include <windows.h>
#include "registers.h"
#include "arithmetic.h"

int zy = 0;
bool sum[8] = {false};
bool carry[8] = {false};

void op_add(){
    Registers reg1;
    cout << endl <<  "OP      REGISTER        VALUE" << endl << "------  --------        --------";
    cout << endl << "add";

    if((reg1.rsrc1[7] != reg1.rsrc2[7]) && (reg1.rsrc1[7] == true)){
        sum[7] = true;
    }
    if((reg1.rsrc1[7] == reg1.rsrc2[7]) && reg1.rsrc1[7] == true){
        carry[7] = true;
    }

    for(zy=6;zy>=0;zy--){
        if((reg1.rsrc1[zy] != reg1.rsrc2[zy]) && (reg1.rsrc1[zy] == true)){
            if((reg1.rsrc1[zy] != reg1.rsrc2[zy]) && (carry[zy+1] != true)){
                sum[zy] = true;
            }
            if(carry[zy+1] == true){
                carry[zy] = true;
            }
        } else if((reg1.rsrc1[zy] == reg1.rsrc2[zy]) && (carry[zy+1] == true)){
            sum[zy] = true;
        }
        if((reg1.rsrc1[zy] == reg1.rsrc2[zy]) && (reg1.rsrc1[zy] == true)){
            carry[zy] = true;
        }
    }

    for(zy=0;zy<8;zy++){
        reg1.rdest[zy] = sum[zy];
    }

    reg1.regvals();
    reg1.Update();
}
