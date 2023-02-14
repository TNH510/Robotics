l1 = 50; l3 = 20; v =10; b =10; h= 100;
for t=0 : 0.1: 10
    t1 = atan2(h - b - l3, v*t);
    t2 = pi/2 - t1;
    l2 = sqrt((h - b -l3)^2 + (v*t)^2) - l1;
    Px = (l1 + l2)*cos(t1) + l3*cos(t1 + t2);
    Py = (l1 + l2)*sin(t1) + l3*sin(t1 + t2);
    subplot(2,2,1);plot(t,t1,'.');
    xlabel('time(s)');ylabel('t1');hold on
    subplot(2,2,2);
    plot(t,t2,'.');
    xlabel('time(s)');ylabel('t2');hold on
    subplot(2,2,3);
    plot(t,l2,'.');
    xlabel('time(s)');ylabel('l2');hold on
    subplot(2,2,4);
    plot(Px,Py,'r+');
    xlabel('Px');ylabel('Py');hold on
    pause(0.1);
    plot(Px,Py,'w+');
    plot(Px,Py,'k.');
    
end