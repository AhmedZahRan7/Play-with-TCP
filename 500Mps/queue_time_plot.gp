set term postscript eps color
set output 'queue.eps'
set ylabel 'queueLen'
set xlabel 'time'
plot 'queue_time.txt' using 1:2
