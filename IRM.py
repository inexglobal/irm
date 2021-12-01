import machine
class IRM:
    def __init__(self):
        self.KEY=-1
        self.timer=-1
    def get(self,pin):
        self.bit = []
        self.bit_t = []
        t = machine.time_pulse_us(pin, 1)
        if(4000<t<5000):
            while (len(self.bit_t)<32):
                t = machine.time_pulse_us(pin, 1)
                self.bit_t.append(t)
            for _tus in self.bit_t:self.bit.append(1 if _tus > 1000 else 0)
            output_verify = 0
            seed = 1
            for x in  self.bit[0:14]:
                if(x == 1):
                    output_verify = output_verify + seed
                seed = seed * 2
            if(output_verify!=16128): return -1
            output_key = 0
            seed = 1
            for x in  self.bit[16:23]:
                if(x == 1):
                    output_key = output_key + seed
                seed = seed * 2
            if(output_verify==16128):
                self.KEY = output_key
                self.timer = 0
                return output_key
        elif(2000<t<3000):
            self.timer=self.timer+1
            if(self.timer>2):
                self.timer=0
                return self.KEY     
        return -1