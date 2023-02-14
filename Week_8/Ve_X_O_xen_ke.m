L = 300; n = 3;l02 = 150; l2 = 220; l3 = 220; l4 = 150;l01 = 60;l1 = 100;r = (L/n)*0.4;

for k = 0:1:(n-1)
    for l = 0:1:(n-1)
        
    if ((mod(l,2) == 0)&&(mod(k,2) == 0))||((mod(l,2) == 1)&&(mod(k,2) == 1))
         i = l; j = k; 
        for I = 0:1:n    
            for X = 0:1:L
                plot3(I*L/n,X,0,'g.');
                hold on;
            end
        end
        
        for J = 0:1:n  
            for Y = 0:1:L
                plot3(Y,J*L/n,0,'g.');
                hold on;
            end
        end

        for t = 0:1:r*sqrt(2)

            xij = (L/n)*(j+0.5);
            yij = (L/n)*(i+0.5);

            x = xij + r/(sqrt(2)) - t;
            y = yij + r/(sqrt(2)) - t;

            A = x+l01;
            B = y-l02;
            c2 = (A^2 + B^2 - l2^2 - l3^2)/(2*l2*l3);
            s2 = sqrt(abs(1 - c2^2));
            t2 = atan2(s2,c2);
            s1 = B*(l3*c2 + l2) - A*(l3*s2);
            c1 = A*(l3*c2 + l2) + B*(l3*s2);
            t1 = atan2(s1,c1);
            Px = l2*cos(t1) + l3*cos(t1 + t2) - l01;
            Py = l2*sin(t1) + l3*sin(t1 + t2) + l02;
            Pz = l1 - l4;
            plot3(Px,Py,0,'.b');
            pause(0.005);
            hold on;
            grid on;

        end

        for t = 0:1:r*sqrt(2)

            xij = (L/n)*(j+0.5);
            yij = (L/n)*(i+0.5);

            x = xij - r/(sqrt(2)) + t;
            y = yij + r/(sqrt(2)) - t;

            A = x+l01;
            B = y-l02;
            c2 = (A^2 + B^2 - l2^2 - l3^2)/(2*l2*l3);
            s2 = sqrt(abs(1 - c2^2));
            t2 = atan2(s2,c2);
            s1 = B*(l3*c2 + l2) - A*(l3*s2);
            c1 = A*(l3*c2 + l2) + B*(l3*s2);
            t1 = atan2(s1,c1);
            Px = l2*cos(t1) + l3*cos(t1 + t2) - l01;
            Py = l2*sin(t1) + l3*sin(t1 + t2) + l02;
            Pz = l1 - l4;
            plot3(Px,Py,0,'.b');
            pause(0.005);
            hold on;
            grid on;

        end
        
        
    end    
        if ((mod(l,2) == 1)&&(mod(k,2) == 0))||((mod(l,2) == 0)&&(mod(k,2) == 1))

            i = l; j = k;         
            for t = 0:0.08:2*pi

            xij = (L/n)*(j+0.5);
            yij = (L/n)*(i+0.5);
            x = xij + r*cos(t);
            y = yij + r*sin(t);
            A = x+l01;
            B = y-l02;
            c2 = (A^2 + B^2 - l2^2 - l3^2)/(2*l2*l3);
            s2 = sqrt(abs(1 - c2^2));
            t2 = atan2(s2,c2);
            s1 = B*(l3*c2 + l2) - A*(l3*s2);
            c1 = A*(l3*c2 + l2) + B*(l3*s2);
            t1 = atan2(s1,c1);
            Px = l2*cos(t1) + l3*cos(t1 + t2) - l01;
            Py = l2*sin(t1) + l3*sin(t1 + t2) + l02;
            Pz = l1 - l4;
            plot3(Px,Py,0,'.r');
            pause(0.01);
            hold on;
            grid on;
            end
        end 
        
    end
end







