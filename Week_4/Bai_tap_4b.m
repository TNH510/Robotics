
syms c1 s1 c2 s2 c3 s3 c4 s4 c5 s5 c6 s6 l1 l2 l3 l4 l5 l6 l7 l8 t1 t2 t3 t4 t5 t6 t7 deta3

Rz1 = [cos(t1) -sin(t1) 0 0; sin(t1) cos(t1) 0 0; 0 0 1 0; 0 0 0 1]

Ry2 = [cos(t2) 0 sin(t2)  0; 0 1 0 0; -sin(t2) 0 cos(t2)  0; 0 0 0 1]
Ry4 = [cos(t4) 0 sin(t4)  0; 0 1 0 0; -sin(t4) 0 cos(t4)  0; 0 0 0 1]

T1 = [1 0 0 l1; 0 1 0 l2; 0 0 1 0; 0 0 0 1]
T2 = [1 0 0 0; 0 1 0 0; 0 0 1 l3; 0 0 0 1]
T3 = [1 0 0 0; 0 1 0 0; 0 0 1 (-l4-l5); 0 0 0 1]
T4 = [1 0 0 l6; 0 1 0 0; 0 0 1 0; 0 0 0 1]

P7 = [0;0;0;1]

%P0 = T(l1,l2,0).R(z,deta1).T(0,0,l3).R(y,deta2).T(0,0,-l4-l5).R(y,deta4).T(l6,0,0).P7
P0 = T1*Rz1*T2*Ry2*T3*Ry4*T4*P7