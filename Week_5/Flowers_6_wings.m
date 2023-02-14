
l1 = 50; l2 = 40;
for t = 0:0.1:30
    X = (1+sin(6*t))*cos(t)*20+50; 
    Y = (1+sin(6*t))*sin(t)*20 ;
    
    c2 = (X^2 + Y^2 -l1^2 - l2^2)/(2*l1*l2);
    s2 = sqrt(abs(1 - c2^2));
    
    t2 = atan2(s2,c2);
    
    c1 = (X*(l1 + l2*c2) + Y*l2*s2)/((l1+l2*c2)^2+(l2*s2)^2);
    s1 = (Y*(l1 + l2*c2) - X*l2*s2)/((l1+l2*c2)^2+(l2*s2)^2);
    
    t1 = atan2(s1,c1);
    
    Px = l1*cos(t1) + l2*cos(t1 + t2);
    Py = l1*sin(t1) + l2*sin(t1 + t2);
    
    subplot(2,1,1);
    plot(t,t1*180/pi,'*',t,t2*180/pi,'^');
    
    hold on
    subplot(2,1,2);
    plot(Px,Py,'*');xlabel('Px');ylabel('Py');
    hold on
end
    
    
    