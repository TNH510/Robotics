
l1 = 50; l2 = 40;
for t = 0:0.05:12*pi
    X = sin(t)*(exp(cos(t))-2*cos(4*t)-sin(t/12)^5)+25; 
    Y = cos(t)*(exp(cos(t))-2*cos(4*t)-sin(t/12)^5) ;
    
    c2 = (X^2 + Y^2 -l1^2 - l2^2)/(2*l1*l2);
    s2 = sqrt(abs(1 - c2^2));
    
    t2 = atan2(s2,c2);
    
    c1 = (X*(l1 + l2*c2) + Y*l2*s2)/((l1+l2*c2)^2+(l2*s2)^2);
    s1 = (Y*(l1 + l2*c2) - X*l2*s2)/((l1+l2*c2)^2+(l2*s2)^2);
    
    t1 = atan2(s1,c1);
    
    Px = l1*cos(t1) + l2*cos(t1 + t2);
    Py = l1*sin(t1) + l2*sin(t1 + t2);
    
    %subplot(2,1,1);
    %plot(t,t1*180/pi,'*',t,t2*180/pi,'^');
    
    %hold on
    %subplot(2,1,2);
    plot(Px,Py,'.');xlabel('Px');ylabel('Py');
    pause(0.06);
    hold on
end
    
    
    