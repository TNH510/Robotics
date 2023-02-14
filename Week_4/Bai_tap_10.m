syms c1 s1 c2 s2 c3 s3 c4 s4 c5 s5 c6 s6 l1 l2 l3 l4 l5 l6 l7 l8 t1 t2 t3 t4 t5 t6 t7
Rz1 = [cos(t1) -sin(t1) 0 0; sin(t1) cos(t1) 0 0; 0 0 1 0; 0 0 0 1]

T1 = [1 0 0 0; 0 1 0 0; 0 0 1 l1; 0 0 0 1]
T2 = [1 0 0 0; 0 1 0 0; 0 0 1 l2; 0 0 0 1]
T3 = [1 0 0 0; 0 1 0 l3; 0 0 1 0; 0 0 0 1]
T4 = [1 0 0 0; 0 1 0 l4; 0 0 1 0; 0 0 0 1]
T5 = [1 0 0 0; 0 1 0 l5; 0 0 1 0; 0 0 0 1]

Rx2 = [1 0 0 0; 0 cos(t2) -sin(t2) 0; 0 sin(t2) cos(t2) 0; 0 0 0 1]
Rx3 = [1 0 0 0; 0 cos(t3) -sin(t3) 0; 0 sin(t3) cos(t3) 0; 0 0 0 1]
Rx4 = [1 0 0 0; 0 cos(t4) -sin(t4) 0; 0 sin(t4) cos(t4) 0; 0 0 0 1]

P9 = [0;0;0;1] 

%P0 = T(0,0,l1).R(z,deta1).T(0,0,l2).R(x,deta2).T(0,l3,0).R(x,deta3).T(0,l4,0).R(x,deta4).T(0,l5,l6).P9
P = T1*Rz1*T2*Rx2*T3*Rx3*T4*Rx4*T5*P9
