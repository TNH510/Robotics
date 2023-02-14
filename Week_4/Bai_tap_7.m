syms c1 s1 c2 s2 c3 s3 c4 s4 c5 s5 c6 s6 l1 l2 l3 l4 l5 l6 l7 l8 t1 t2 t3 t4 t5 t6 t7
Rz1 = [cos(t1) -sin(t1) 0 0; sin(t1) cos(t1) 0 0; 0 0 1 0; 0 0 0 1]
Rz2 = [cos(t2) -sin(t2) 0 0; sin(t2) cos(t2) 0 0; 0 0 1 0; 0 0 0 1]
Rz3 = [cos(t3) -sin(t3) 0 0; sin(t3) cos(t3) 0 0; 0 0 1 0; 0 0 0 1]

T1 = [1 0 0 0; 0 1 0 0; 0 0 1 l1; 0 0 0 1]
T2 = [1 0 0 0; 0 1 0 l4; 0 0 1 l2; 0 0 0 1]
T3 = [1 0 0 0; 0 1 0 l5; 0 0 1 l3; 0 0 0 1]
T4 = [1 0 0 0; 0 1 0 0; 0 0 1 -l6; 0 0 0 1]
T5 = [1 0 0 0; 0 1 0 0; 0 0 1 -l7; 0 0 0 1]

P6 = [0;0;0;1] 

%P0 = T(0,0,l1).R(z,deta1).T(0,l4,l2).R(z,deta2).T(0,l5,l3).T(0,0,-l6).R(z,deta3).T(0,0,-l7).P6
P = T1*Rz1*T2*Rz2*T3*T4*Rz3*T5*P6
