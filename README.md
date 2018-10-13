# Testbench Process Generator

## A simple script useful to quickly generate test vectors to be implemented in VHDL testbenches.

### INSTALLATION:

1. Download code (*Clone or Download* button).
2. Extract zip
3. Open ** folder using ```cd ```
4. Run script (usage below).

### USAGE:
* ### Must insert at least one signal, a time interval and a time unit:

    ```bash
    python3 testVectorsGenerator.py <signal1> <signal2> ... <signalN> <Time_Interval> <Time_Unit>
    ```

### EXAMPLE:

```
python3 testVectorsGenerator.py a b c d 10 ns
To be generated: 16 different cases.
a
b
c
d
TimeInterval: 10
TimeUnit: ns


----Copy-Paste the following code----
```
```VHDL
process
        begin
                a <= '0'; b <= '0'; c <= '0'; d <= '0'; 
                wait for 10 ns;
                a <= '0'; b <= '0'; c <= '0'; d <= '1'; 
                wait for 10 ns;
                a <= '0'; b <= '0'; c <= '1'; d <= '0'; 
                wait for 10 ns;
                a <= '0'; b <= '0'; c <= '1'; d <= '1'; 
                wait for 10 ns;
                a <= '0'; b <= '1'; c <= '0'; d <= '0'; 
                wait for 10 ns;
                a <= '0'; b <= '1'; c <= '0'; d <= '1'; 
                wait for 10 ns;
                a <= '0'; b <= '1'; c <= '1'; d <= '0'; 
                wait for 10 ns;
                a <= '0'; b <= '1'; c <= '1'; d <= '1'; 
                wait for 10 ns;
                a <= '1'; b <= '0'; c <= '0'; d <= '0'; 
                wait for 10 ns;
                a <= '1'; b <= '0'; c <= '0'; d <= '1'; 
                wait for 10 ns;
                a <= '1'; b <= '0'; c <= '1'; d <= '0'; 
                wait for 10 ns;
                a <= '1'; b <= '0'; c <= '1'; d <= '1'; 
                wait for 10 ns;
                a <= '1'; b <= '1'; c <= '0'; d <= '0'; 
                wait for 10 ns;
                a <= '1'; b <= '1'; c <= '0'; d <= '1'; 
                wait for 10 ns;
                a <= '1'; b <= '1'; c <= '1'; d <= '0'; 
                wait for 10 ns;
                a <= '1'; b <= '1'; c <= '1'; d <= '1'; 
                wait for 10 ns;
                wait;
        end process;
```
```
-------------------------------------
```