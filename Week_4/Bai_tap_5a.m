syms c1 s1 c2 s2 c3 s3 c4 s4 c5 s5 c6 s6 l1 l2 l3 l4 l5 l6 l7 l8 t1 t2 t3 t4 t5 t6 t7
Ry1 = [cos(t1) 0 sin(t1)  0; 0 1 0 0; -sin(t1) 0 cos(t1)  0; 0 0 0 1]
Ry3 = [cos(t3) 0 sin(t3)  0; 0 1 0 0; -sin(t3) 0 cos(t3)  0; 0 0 0 1]

T1 = [1 0 0 0; 0 1 0 0; 0 0 1 -l1; 0 0 0 1]
T2 = [1 0 0 0; 0 1 0 0; 0 0 1 -l2; 0 0 0 1]


P4 = [0;0;0;1] 

%P0 = R(y,deta1).T(0,0,-l1).R(y,deta3).T(0,0,-l2).P4

P = Ry1*T1*Ry3*T2*P4



