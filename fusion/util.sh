define xt
	target remote fusion:9898
	file level00/level00
	set sysroot remote:
end

define xni
	ni
	x/10i $pc
	info reg
end

define xsi
	si
	x/10i $pc
	info reg
end

