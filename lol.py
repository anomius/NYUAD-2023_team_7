#plot
area=[1,2,3]
yeild=[0.1,0.2,0.3]
soil=[0.1,0.2,0.3]

#plant
price=[[100,150],[200,150],[300,350]]
fertizer_need=[0.1,-0.2,0.3]
impactFactor=[0.1,1.2,0.3]

#enviorment varialbe
fertilizer_price=0.1
Enviorment = 0.1

#i -> plant
#j -> plot
#k -> time
I,J,K=2,2,2

class PlantOpp:
    def __init__(self,area,yeild,soil,price,fertizer_need,impactFactor,fertilizer_price,Enviorment,I,J,K):
        self.area=area
        self.yeild=yeild
        self.soil=soil
        self.price=price
        self.fertizer_need=fertizer_need
        self.impactFactor=impactFactor
        self.fertilizer_price=fertilizer_price
        self.Enviorment=Enviorment
        self.I=I
        self.J=J
        self.K=K
    
    def find_liner_coffecent(self):
        liner=[[[0 for i in range(self.I+1)] for j in range(self.J+1)] for k in range(self.K+1)]
        #find the coffecent of the liner equation
        #financial benifit at k=0
        k=0
        for i in range(self.I):
            for j in range(self.J):
                    liner[i][j][k]=self.area[j]*self.yeild[j]*self.price[i][k]
        
        #enviormental benifit
        for i in range(self.I):
            for j in range(self.J):
                for k in range(self.K):
                    liner[i][j][k]-=(self.Enviorment*self.fertizer_need[i])/(self.soil[j]*self.impactFactor[i])
        
        # fertizer loss
        for i in range(self.I):
            for j in range(self.J):
                for k in range(self.K):
                    liner[i][j][k]-=(self.fertizer_need[i]*self.fertilizer_price)/(self.soil[j]*self.yeild[j])
        l_coff=[0 for i in range(self.I*self.J*self.K)]
        for i in range(self.I):
            for j in range(self.J):
                for k in range(self.K):
                    l_coff[(((i*I)+j)*J)+k]=liner[i][j][k]
        return l_coff
                
    def find_quad_coffent(self):
        quad=[[0 for k in range(self.I*self.J*self.K)] for i in range(self.I*self.J*self.K)]
        k=1
        for i in range(self.I):
            for j in range(self.J):
                for Q_i in range(self.I):
                    for Q_j in range(self.J):
                        Q_k=0
                        quad[int((((i*I)+j)*J)+k)][int((((i*Q_i)+j)*Q_j)+k)]+=self.area[j]*self.yeild[j]*self.price[i][k]*self.impactFactor[Q_i]
        
        # fertizer loss
        for i in range(self.I):
            for j in range(self.J):
                for Q_i in range(self.I):
                    for Q_j in range(self.J):
                        quad[int((((i*I)+j)*J)+k)][int((((i*Q_i)+j)*Q_j)+k)]-=((self.fertizer_need[i]*self.fertilizer_price)/(self.soil[j]*self.yeild[j]*self.impactFactor[Q_i]))
        
        return quad

    def create_constraints(self):
        constraints=[]
        for j in range(self.J):
            for k in range(self.K):
                l=[0 for i in range(self.I*self.J*self.K)]  
                for i in range(self.I):
                    l[((((i*I)+j)*J)+k)] = 1
                print(l)
                constraints.append([l,[1.0,"<="]])
        return constraints
                

            
f=PlantOpp(area,yeild,soil,price,fertizer_need,impactFactor,fertilizer_price,Enviorment,I,J,K)
print(f.find_liner_coffecent())
print(f.find_quad_coffent()) 
print(f.create_constraints())