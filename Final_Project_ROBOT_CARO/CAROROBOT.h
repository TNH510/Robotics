#include <AccelStepper.h>
#include <MultiStepper.h>
#include <math.h>

#define pi 3.14159265
#define Enable 8

void SETUP_ROBOT();
void Move(float x, float y);
void Move_ban_co(float x, float y);
void Test_Motor_X();
void Test_Motor_Y();
void Test_Motor_Z();
void Test_Move_funtion();
void Draw_Heart();
void Draw_X(int X_R,int Y_R);
void Draw_Circle(int radius, int X_R,int Y_R);
void set_home_Y();
void set_home_X();
void set_home();
void set_home_no_switch();
void z_down();
void X_home();
void Y_home();
void z_home();
void set_speed_XY(int speedXY, int maxspeedXY, int a_XY);
void move_to_number_3x3(int numberX, int numberY);
int X_3(int X);
int Y_3(char Y);
int X_5(int X);
int Y_5(char Y);
int X_7(int X);
int Y_7(char Y);
void Draw_Circle_3(int X_R,int Y_R);
void Draw_Circle_5(int X_R,int Y_R);
void Draw_Circle_7(int X_R,int Y_R);
void Draw_X_3(int X_R,int Y_R);
void Draw_X_5(int X_R,int Y_R);
void Draw_X_7(int X_R,int Y_R);
