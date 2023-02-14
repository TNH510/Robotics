#include <AccelStepper.h>
#include <MultiStepper.h>
#include <math.h>

#define pi 3.14159265
#define Enable 8
  AccelStepper stepperX(1, 2, 5);
  AccelStepper stepperY(1, 3, 6);
  AccelStepper stepperZ(1, 4, 7);
  int Steps, Steps_X, Steps_Y, theta_1, theta_2, x_home, y_home; 
  int K = 0; 
  float do_dai, X,Y;
void SETUP_ROBOT() {
  
  Serial.begin(9600);
  pinMode(2,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(7,OUTPUT);
  pinMode(9,INPUT_PULLUP);//x
  pinMode(10,INPUT_PULLUP);//y
  pinMode(11,INPUT_PULLUP);//z
  pinMode(Enable,OUTPUT);
  stepperX.setMaxSpeed(6000);
  stepperX.setSpeed(1500);
  stepperX.setAcceleration(5000);
  stepperY.setMaxSpeed(6000);
  stepperY.setSpeed(1500);
  stepperY.setAcceleration(5000);
  stepperZ.setMaxSpeed(5000);
  stepperZ.setSpeed(3000);
  stepperZ.setAcceleration(3000);
  stepperY.setPinsInverted(3);
  digitalWrite(Enable, LOW);
}

void z_down()
{          
      do_dai= -12;
      Steps = do_dai*200*2*2/2;
      stepperZ.moveTo(Steps);
      while(stepperZ.distanceToGo()!=0)
        {
          stepperZ.run();
        }  
}

void z_home()
{          

    stepperZ.moveTo(0);
    while(stepperZ.distanceToGo()!=0)
    {
      stepperZ.run();
    }
}

void X_home()
{          

    stepperX.moveTo(0);
    while(stepperX.distanceToGo()!=0)
    {
      stepperX.run();
    }
}

void Y_home()
{          

    stepperY.moveTo(0);
    while(stepperY.distanceToGo()!=0)
    {
      stepperY.run();
    }
}

void set_speed_XY(int speedXY, int maxspeedXY, int a_XY)
{
  stepperX.setMaxSpeed(maxspeedXY);
  stepperX.setSpeed(speedXY);
  stepperX.setAcceleration(a_XY);
  stepperY.setMaxSpeed(maxspeedXY);
  stepperY.setSpeed(speedXY);
  stepperY.setAcceleration(a_XY);
}

void set_home_Y()
{ 
  stepperY.setMaxSpeed(1000);
  stepperY.setSpeed(500);
  stepperY.setAcceleration(2000);
  int P = 0;
  stepperY.moveTo(5000);
  while ((stepperY.distanceToGo()!=0)&&(P == 0))
    {stepperY.run();if (digitalRead(10) == 0){P = 1;delay(200);Serial.println("SET HOME Y");stepperY.setCurrentPosition(0);}}
   
}
void set_home_X()
{ 
  int P = 0;
  stepperX.setMaxSpeed(1000);
  stepperX.setSpeed(500);
  stepperX.setAcceleration(2000);
  
  stepperX.moveTo(5000);
  while ((stepperX.distanceToGo()!=0)&&(P == 0))
    {stepperX.run();if (digitalRead(9) == 0){P = 1;delay(200);Serial.println("SET HOME X");stepperX.setCurrentPosition(0);}}
   
}
void set_home()
{
  set_home_Y();
  set_home_X();
  
}

void set_home_no_switch()
{
  Y_home();
  X_home();
  
}

void Move(float x, float y)
{
  float A, B;
  double c2,s2,t2,c1,s1,t1;
  float l2 = 220; 
  float l3 = 220; 
  float l01 = 0;
  float l02 = 0;
  A = x - l01;
  B = y + l02;
  c2 = (pow(A,2) + pow(B,2) - pow(l2,2) - pow(l3,2))/(2*l2*l3);
  s2 = sqrt(abs(1 - pow(c2,2)));
  t2 = atan2(s2,c2)*180/pi;
  s1 = B*(l3*c2  + l2) - A*(l3*s2);
  c1 = A*(l3*c2 + l2) + B*(l3*s2);
  t1 = atan2(s1,c1)*180/pi;
  Steps_X = (t1)*20*2*2/3;  
  stepperX.moveTo(-1*Steps_X);
  Steps_Y = (t2)*2*2*20/3;
  stepperY.moveTo(-1*Steps_Y);
  Serial.println(t1);
  Serial.println(t2);
  while((stepperX.distanceToGo()!=0) || (stepperY.distanceToGo()!=0))
  {
    stepperX.run();
    stepperY.run();  
  }
}

void Move_ban_co(float x, float y)
{
  Move(x-150,y+90);//robot cach canh trai 150mm, cach canh duoi 130mm
}

void Test_Motor_X()
{
    Serial.println("Enter Angle (degrees): ");
    while(Serial.available()==0){};
    delay(4000);
    theta_1 = Serial.parseInt();
    Serial.println(theta_1);
    Steps = theta_1*20*2*2/3; 
    stepperX.moveTo(-1*Steps);
    while(stepperX.distanceToGo()!=0)
    {
      stepperX.run();
    }
}

void Test_Motor_Y()
{
    Serial.println("Enter Angle (degrees): ");
    while(Serial.available()==0){};
    delay(4000);
    theta_2 = Serial.parseInt();
    Serial.println(theta_2);
    Steps = theta_2*2*2*20/3;
      
    stepperY.moveTo(Steps);
    while(stepperY.distanceToGo()!=0)
    {
      stepperY.run();
    } 
    
}

void Test_Motor_Z()
{   
    stepperZ.setCurrentPosition(0);
    Serial.println("Enter distance (mm): ");
    while(Serial.available()==0){};
    delay(4000);
    do_dai= Serial.parseFloat();
    Serial.println(do_dai);
    Steps = do_dai*200*2*2/2;
    stepperZ.moveTo(Steps);
    while(stepperZ.distanceToGo()!=0)
    {
      stepperZ.run();
    }
    
}

void Test_Move_funtion()
{
    Serial.println("Enter X: ");
    while(Serial.available()==0){};
    delay(4000);
    X = Serial.parseInt();
    Serial.println(X);
    Serial.println("Enter Y: ");
    while(Serial.available()==0){};
    delay(4000);
    Y = Serial.parseInt();
    Serial.println(Y);
    Move_ban_co(X,Y);
}

void Draw_Heart()
{   
    stepperZ.setCurrentPosition(0);
    for (float t = -1; t < 2*pi + 0.5; t = t+0.005)
    { 
        X = -100 + 32*pow(sin(t),3)*3/2;
        Y = 300 + 26*cos(t)*3/2 - 10*cos(2*t)*3/2 - 4*cos(3*t)*3/2 - 2*cos(4*t)*3/2;
        Move_ban_co(X,Y);  
        z_down();         
    }
    delay(2000);
    z_home();
    set_home_no_switch();   
}

void Draw_X(int r, int X_R,int Y_R)
{   
    set_speed_XY(3000,6500,6000);
    stepperZ.setCurrentPosition(0);
    int K = 0;
    for (float t = 0 ;t < r*sqrt(2);t = t + 0.4)
    { 

            X = X_R - r/(sqrt(2)) + t;
            Y = Y_R + r/(sqrt(2)) - t;
            Move_ban_co(X,Y);
            z_down();
    }
    for (float t = 0 ;t < r*sqrt(2);t = t + 0.4)
    {       
            if (K == 0) {z_home(); K = 1;}
            X = X_R + r/(sqrt(2)) - t;
            Y = Y_R + r/(sqrt(2)) - t;
            Move_ban_co(X,Y);
            z_down();
    }
    delay(500);
    z_home();
    set_home_no_switch();
}

void Draw_Circle(int radius, int X_R,int Y_R)
{   
    stepperZ.setCurrentPosition(0);
    set_speed_XY(1000,4000,4500);
    for (float t = -0.1; t <pi/2 ; t = t+0.01)
    { 
           X = X_R + radius*sin(t);
           Y = Y_R + radius*cos(t);
           Move_ban_co(X,Y);    
           z_down();
    }
    set_speed_XY(3000,6500,6000);
    for (float t = pi/2; t < pi ; t = t+0.007)
    { 
            X = X_R + radius*sin(t);
            Y = Y_R + radius*cos(t);
            Move_ban_co(X,Y);
            
    }
    set_speed_XY(1000,4000,4500);
    for (float t = pi; t <3*pi/2 ; t = t+0.01)
    { 
            X = X_R + radius*sin(t);
            Y = Y_R + radius*cos(t);
            Move_ban_co(X,Y);
            
    }
    set_speed_XY(3000,6500,6000);
    for (float t = 3*pi/2; t <2*pi+0.1 ; t = t+0.007)
    { 
            X = X_R + radius*sin(t);
            Y = Y_R + radius*cos(t);
            Move_ban_co(X,Y);          
    }
    delay(500);
    z_home();
    set_home_no_switch();
 
}
void move_to_number_3x3(int numberX, int numberY)//o vuong ban co 3x3
{
  float X, Y;
  X = 100*(numberX+0.5);
  Y = 100*(numberY+0.5);
  Move_ban_co(X,Y);
}

int X_3(int X)
{
  if (X == 1) return 50;
  else if (X == 2) return 150;
  else if (X == 3) return 250;
  
}
int Y_3(char Y)
{
  if (Y == 'A') return 50;
  else if (Y == 'B') return 150;
  else if (Y == 'C') return 250;
  
}

int X_5(int X)
{
  if (X == 1) return 30;
  else if (X == 2) return 90;
  else if (X == 3) return 150;
  else if (X == 4) return 210;
  else if (X == 5) return 270;
  
}
int Y_5(char Y)
{
  if (Y == 'A') return 30;
  else if (Y == 'B') return 90;
  else if (Y == 'C') return 150;
  else if (Y == 'D') return 210;
  else if (Y == 'E') return 270;
  
}


int X_7(int X)
{
  if (X == 1) return 21;
  else if (X == 2) return 64;
  else if (X == 3) return 107;
  else if (X == 4) return 150;
  else if (X == 5) return 192;
  else if (X == 6) return 235;
  else if (X == 7) return 279;
  
}
int Y_7(char Y)
{
  if (Y == 'A') return 21;
  else if (Y == 'B') return 64;
  else if (Y == 'C') return 107;
  else if (Y == 'D') return 150;
  else if (Y == 'E') return 192;
  else if (Y == 'F') return 235;
  else if (Y == 'G') return 279;
  
}

void Draw_Circle_3(int X_R,int Y_R)
{
  Draw_Circle(40,X_R,Y_R);
}

void Draw_Circle_5(int X_R,int Y_R)
{
  Draw_Circle(25,X_R,Y_R);
}

void Draw_Circle_7(int X_R,int Y_R)
{
  Draw_Circle(15,X_R,Y_R);
}

void Draw_X_3(int X_R,int Y_R)
{
  Draw_X(45,X_R,Y_R);
}

void Draw_X_5(int X_R,int Y_R)
{
  Draw_X(26,X_R,Y_R);
}

void Draw_X_7(int X_R,int Y_R)
{
  Draw_X(11,X_R,Y_R);
}
