syms c1 s1 c2 s2 c3 s3 c4 s4 c5 s5 c6 s6 l1 l2 l3 l4 l5 l6 l7 l8 t1 t2 t3 t4 t5 t6 t7

Rz2 = [cos(t2) -sin(t2) 0 0; sin(t2) cos(t2) 0 0; 0 0 1 0; 0 0 0 1]
Rz3 = [cos(t3) -sin(t3) 0 0; sin(t3) cos(t3) 0 0; 0 0 1 0; 0 0 0 1]
Rz4 = [cos(t4) -sin(t4) 0 0; sin(t4) cos(t4) 0 0; 0 0 1 0; 0 0 0 1]

Ry1 = [cos(t1) 0 sin(t1)  0; 0 1 0 0; -sin(t1) 0 cos(t1)  0; 0 0 0 1]
Ry5 = [cos(t5) 0 sin(t5)  0; 0 1 0 0; -sin(t5) 0 cos(t5)  0; 0 0 0 1]

T1 = [1 0 0 l1; 0 1 0 0; 0 0 1 0; 0 0 0 1]
T2 = [1 0 0 0; 0 1 0 l2; 0 0 1 0; 0 0 0 1]
T3 = [1 0 0 0; 0 1 0 l3; 0 0 1 0; 0 0 0 1]
T4 = [1 0 0 0; 0 1 0 l4; 0 0 1 0; 0 0 0 1]
T5 = [1 0 0 0; 0 1 0 l5; 0 0 1 0; 0 0 0 1]
T6 = [1 0 0 0; 0 1 0 l6; 0 0 1 0; 0 0 0 1]

P11 = [0;0;0;1] 

%P0 = R(y,deta1).T(l1,0,0).T(0,l2,0).R(z,deta2).T(0,l3,0).R(z,deta3).T(0,l4,0).R(z,deta4).T(0,l5,0).R(y,deta5).T(l6,0,0).P11

P = Ry1*T1*T2*Rz2*T3*Rz3*T4*Rz4*T5*Ry5*T6*P11
