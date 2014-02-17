def ct(m,n){
        return ((n*n+n) * (m*m+m)) / 4
}

diff=1000000

def bits=[]

quad={ a,b,c -> (-b + Math.sqrt(b**2 - 4*a*c))/(2*a) }

upper=quad(1, 1, -4000000).toInteger()

for(i in 1..upper) {
        for(j in i..upper) {
                x=ct(i,j)
                new_diff=Math.abs(2000000-x)
                if ((x + new_diff) > (2000000 + diff)) {
                        break
                }
                if (new_diff < diff) {
                        diff=new_diff
                        bits=[]
                        bits.add(x)
                        bits.add(i)
                        bits.add(j)
                        bits.add(i*j)
                }
        }
}

println bits[0]
println bits[1]
println bits[2]
println bits[3]
