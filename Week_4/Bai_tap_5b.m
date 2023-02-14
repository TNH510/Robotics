syms c1 s1 c2 s2 c3 s3 c4 s4 c5 s5 c6 s6 l1 l2 l3 l4 l5 l6 l7 l8 t1 t2 t3 t4 t5 t6 t7 deta3
Rx1 = [1 0 0 0; 0 cos(t1) -sin(t1) 0; 0 sin(t1) cos(t1) 0; 0 0 0 1]

T1 = [1 0 0 0; 0 1 0 0; 0 0 1 (-l1-cos(deta3)*l2); 0 0 0 1]

P2 = [0;0;0;1] 

%P0 = R(x,deta2).T(0,0,-l1-cos(deta3)*l2).P2

P0 = Rx1*T1*P2



