#include <AccelStepper.h>
#include <MultiStepper.h>
#include <math.h>
#include "CAROROBOT.h"
int mode,radius,X_R,Toa_do,Y_R,_X;
char _Y, Ki_tu_choi;
void setup() {SETUP_ROBOT();}
void loop()
{   
    
    while(Serial.available()==0){};
    mode = Serial.parseInt();
    
    while(mode == 3)
    {
      
      while(Serial.available()==0){};
      Ki_tu_choi = Serial.read();
      while(Ki_tu_choi == 'o')
      {
        
        while(Serial.available()==0){};
        Toa_do = Serial.parseInt();
        _X = Toa_do % 3 ;
        if ((Toa_do % 3)== 0) {_X = 3;}
        if ((1 <= Toa_do)&&(Toa_do <=3))   {_Y = 'A';}
        else if ((4 <= Toa_do)&&(Toa_do <=6))  {_Y = 'B';}
        else if ((7 <= Toa_do)&&(Toa_do <=9))  {_Y = 'C';}
        Draw_Circle_3(X_3(_X),Y_3(_Y));
      }

      while(Ki_tu_choi == 'x')
      {
        
        while(Serial.available()==0){};
        Toa_do = Serial.parseInt();
        _X = Toa_do % 3 ;
        if ((Toa_do % 3)== 0) {_X = 3;}
        if ((1 <= Toa_do)&&(Toa_do <=3))   {_Y = 'A';}
        else if ((4 <= Toa_do)&&(Toa_do <=6))  {_Y = 'B';}
        else if ((7 <= Toa_do)&&(Toa_do <=9))  {_Y = 'C';}
        Draw_X_3(X_3(_X),Y_3(_Y));
      }

      mode = 9999;

    }

    while(mode == 5)
    {
      
      while(Serial.available()==0){};
      Ki_tu_choi = Serial.read();
      while(Ki_tu_choi == 'o')
      {
        
        while(Serial.available()==0){};
        Toa_do = Serial.parseInt();
        _X = Toa_do % 5 ;
        if ((Toa_do % 5)==0) {_X = 5;}
        if ((1 <= Toa_do)&&(Toa_do <=5))   {_Y = 'A';}
        else if ((6 <= Toa_do)&&(Toa_do <=10))  {_Y = 'B';}
        else if ((11 <= Toa_do)&&(Toa_do <=15))  {_Y = 'C';}
        else if ((16 <= Toa_do)&&(Toa_do <=20))  {_Y = 'D';}
        else if ((21 <= Toa_do)&&(Toa_do <=25))  {_Y = 'E';}
        
        Draw_Circle_5(X_5(_X),Y_5(_Y));
      }

      while(Ki_tu_choi == 'x')
      {
        
        while(Serial.available()==0){};
        Toa_do = Serial.parseInt();
        _X = Toa_do % 5 ;
        if ((Toa_do % 5)==0) {_X = 5;}
        if ((1 <= Toa_do)&&(Toa_do <=5))   {_Y = 'A';}
        else if ((6 <= Toa_do)&&(Toa_do <=10))  {_Y = 'B';}
        else if ((11 <= Toa_do)&&(Toa_do <=15))  {_Y = 'C';}
        else if ((16 <= Toa_do)&&(Toa_do <=20))  {_Y = 'D';}
        else if ((21 <= Toa_do)&&(Toa_do <=25))  {_Y = 'E';}
        
        Draw_X_5(X_5(_X),Y_5(_Y));
      }

      mode = 9999;

    }

    while(mode == 7)
    {
      
      while(Serial.available()==0){};
      Ki_tu_choi = Serial.read();
      while(Ki_tu_choi == 'o')
      {
        
        while(Serial.available()==0){};
        Toa_do = Serial.parseInt();
        _X = Toa_do % 7 ;
        if ((Toa_do % 7)==0) {_X = 7;}
        if ((1 <= Toa_do)&&(Toa_do <=7))   {_Y = 'A';}
        else if ((8 <= Toa_do)&&(Toa_do <=14))  {_Y = 'B';}
        else if ((15 <= Toa_do)&&(Toa_do <=21))  {_Y = 'C';}
        else if ((22 <= Toa_do)&&(Toa_do <=28))  {_Y = 'D';}
        else if ((29 <= Toa_do)&&(Toa_do <=35))  {_Y = 'E';}
        else if ((36 <= Toa_do)&&(Toa_do <=42))  {_Y = 'F';}
        else if ((43 <= Toa_do)&&(Toa_do <=49))  {_Y = 'G';}
        
        Draw_Circle_7(X_7(_X),Y_7(_Y));
      }

      while(Ki_tu_choi == 'x')
      {
        
        while(Serial.available()==0){};
        Toa_do = Serial.parseInt();
        _X = Toa_do % 7 ;
        if ((Toa_do % 7)==0) {_X = 7;}
        if ((1 <= Toa_do)&&(Toa_do <=7))   {_Y = 'A';}
        else if ((8 <= Toa_do)&&(Toa_do <=14))  {_Y = 'B';}
        else if ((15 <= Toa_do)&&(Toa_do <=21))  {_Y = 'C';}
        else if ((22 <= Toa_do)&&(Toa_do <=28))  {_Y = 'D';}
        else if ((29 <= Toa_do)&&(Toa_do <=35))  {_Y = 'E';}
        else if ((36 <= Toa_do)&&(Toa_do <=42))  {_Y = 'F';}
        else if ((43 <= Toa_do)&&(Toa_do <=49))  {_Y = 'G';}
        
        Draw_X_7(X_7(_X),Y_7(_Y));
      }

      mode = 9999;

    }

    if (mode == 102)
    {
        Move_ban_co(150,150);
        Move(440,0);  
    }
    if (mode == 101)
    {
        Move_ban_co(150,150);
        Move(440,0);  
    }
    if (mode == 100)
    {   
        Move_ban_co(150,0);
        z_down();
        z_home();
        delay(1000);
        Move_ban_co(0,0);
        z_down();
        z_home();
        Move_ban_co(0,300);
        z_down();
        z_home();
        Move_ban_co(300,300);
        z_down();
        z_home();
        Move_ban_co(300,0);
        z_down();
        z_home();
        set_home_no_switch();
    }
    /*if (mode == 101)
    {
        Test_Motor_Z();
    }*/
    
 
}
