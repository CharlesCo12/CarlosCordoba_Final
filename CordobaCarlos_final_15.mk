CordobaCarlos_final_15.pdf: datos.dat plot15.py
	python plot15.py

%.dat : a.out
	./a.out 

a.out: datos15.cpp
	g++ datos15.cpp
