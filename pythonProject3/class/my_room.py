from function.exam.room import TV

TV1= TV()
TV2= TV()

TV1.inch=50
TV2.inch=60
TV2.channel=10

TV2.print_inch()
TV2.tv_on_off()
TV2.change_channel(15)
TV2.tv_on_off()


print(TV1)
print(TV2)