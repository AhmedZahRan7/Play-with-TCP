set term postscript eps color
set output 'packet_delay.eps'
set ylabel 'delay'
set xlabel 'time'
plot 'packet_delay.txt' using 1:2
