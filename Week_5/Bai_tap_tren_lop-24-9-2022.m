l1 = 40; l2 = 50; l3 = 40; 
xA = 30 ; yA = 30 ; zA = 30; 
xB = 70 ; yB = 70 ; zB = 30;

for t= 0:0.01:1
    x = xA + (xB - xA)*t;
    y = yA + (yB - yA)*t;
    z = 30;
    
    t1 = atan2(-x,y);
    
    A = -x/sin(t1);
    B = z - l1;
    c3 = (A^2 + B^2 - l2^2 - l3^2)/(2*l2*l3);
    
    s3 = sqrt(abs(1 - c3^2));
    t3 = atan2(s3,c3);
    
    c2 = A*(l2 + l3*c3) + B*(s3*l3);
    s2 = (l2 + l3*c3)*B - A*(l3*s3);
    t2 = atan2(s2,c2);    
    
    px = -sin(t1)*(l2*cos(t2) + l3*cos(t2 + t3));
    py = cos(t1)*(cos(t2+t3)*l3 + cos(t2)*l2);
    pz = sin(t2+t3)*l3 + sin(t2)*l2 +l1;
     
    
    subplot(2,2,1);
    plot(t,t1*180/pi,'b.');grid on;title('Theta 1');
    xlabel('Time (s)');ylabel('Angle (Degree)');hold on
    subplot(2,2,2);
    plot(t,t2*180/pi,'g.');grid on;title('Theta 2');
    xlabel('Time (s)');ylabel('Angle (Degree)');hold on
    subplot(2,2,3);
    plot(t,t3*180/pi,'r.');grid on;title('Theta 3');
    xlabel('Time (s)');ylabel('Angle (Degree)');hold on
    subplot(2,2,4);
    plot3(px,py,pz,'r.');grid on;
    pause(0.1);
    xlabel('Px (cm)');ylabel('Py (cm)');zlabel('Pz (cm)');hold on
   
    
    
end