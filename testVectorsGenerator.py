import sys

def CheckArgs():
   
    signals = []

    num_args = len(sys.argv) - 1
    if (num_args == 0):
        print("Must insert at least one argument!")
        print("\nUSAGE: python3 testVectorsGenerator.py <signal1> <signal2> ... <signalN> <Time_Interval> <Time_Unit>")
        sys.exit("\n\nExiting, please re-launch the application following the previous instruction.")

    num_signals = num_args - 2
    num_cases = 2**num_signals
    print("To be generated: " + str(num_cases) + " different cases.")
    for i in range(1, num_signals + 1):
        signals.append(sys.argv[i])
        print(str(signals[i-1]))
    
    timeInterval = sys.argv[num_args - 1]
    timeUnit = sys.argv[num_args]

    print("TimeInterval: " + str(timeInterval))
    print("TimeUnit: " + str(timeUnit))
    
    return (num_cases, num_signals, signals, timeInterval, timeUnit)

def ProcessGeneration(num_cases, num_signals, signals, timeInterval, timeUnit):
    print("\n\n----Copy-Paste the following code----\n")
    print("process")
    print("begin")
    
    for i in range(0, num_cases):
        string = "{0:0" + str(num_signals) + "b}"
        binaryConverted = str(string.format(i))

        print("\t", end='')
        for j in range(0, len(binaryConverted)):
            print(signals[j] + " <= \'" + binaryConverted[j] + "\'; ", end='')
        print("\n\twait for " + str(timeInterval) + " " + str(timeUnit) + ";")
    
    print("\twait;")
    print("end process;")

    print("\n-------------------------------------")


if __name__ == '__main__':

    (num_cases, num_signals, signals, timeInterval, timeUnit) = CheckArgs()
    ProcessGeneration(num_cases, num_signals, signals, timeInterval, timeUnit)
