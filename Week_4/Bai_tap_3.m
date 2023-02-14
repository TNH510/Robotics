
syms c1 s1 c2 s2 c3 s3 c4 s4 c5 s5 c6 s6 l1 l2 l3 l4 l5 l6 l7 l8 t1 t2 t3 t4 t5 t6 t7 

Rz1 = [cos(t1) -sin(t1) 0 0; sin(t1) cos(t1) 0 0; 0 0 1 0; 0 0 0 1]
Rz2 = [cos(t2) -sin(t2) 0 0; sin(t2) cos(t2) 0 0; 0 0 1 0; 0 0 0 1]
Rz3 = [cos(t3) -sin(t3) 0 0; sin(t3) cos(t3) 0 0; 0 0 1 0; 0 0 0 1]
Rz4 = [cos(t4) -sin(t4) 0 0; sin(t4) cos(t4) 0 0; 0 0 1 0; 0 0 0 1]

T1 = [1 0 0 l2; 0 1 0 l1; 0 0 1 0; 0 0 0 1]
T2 = [1 0 0 l4; 0 1 0 0; 0 0 1 l3; 0 0 0 1]
T3 = [1 0 0 l5; 0 1 0 0; 0 0 1 0; 0 0 0 1]
T4 = [1 0 0 l7; 0 1 0 l6; 0 0 1 -l8; 0 0 0 1]

P4 = [0;0;0;1]

%P0 = R(z,deta1).T(l2,0,l1).R(z,deta2).T(l4,0,l3).R(z,deta3).T(l5,0,0).R(z,deta4).T(l7,l6,-l8).P4
P0 = Rz1*T1*Rz2*T2*Rz3*T3*Rz4*T4*P4