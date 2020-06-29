# ptr_lib

A library in Python of resources for Geomatics, GNSS Analysis and Transportation Engineering. 

2014-2020. Developed by Laboratory of Geodesy and Topography - Polytechnic School of University of Sao Paulo (Desenvolvido pelo Laboratório de Geodesia e Topografia - Departamento de Engenharia de Transportes - Escola Politécnica da Universidade de São Paulo) 

Authors: 
* R.Pissardini - B.Sc.Computer Science, M.Sc. Transportation Engineering
* A.Boava Meza
-------------

# Installation

* Download .zip file;
* Enter in /ptr_lib_master directory and run the command

```
python setup.py sdist bdist_wheel
```

* Enter in /dist/ directory and run 
```
pip install NAME_OF_FILE.wh*
```

-------------

# Third-party software

Some functions in PTR-LIB require third-party software for efficient operation. Check the need to download these software. We list these software that, in some cases, may have different licenses from the present library:

* [Teqc](https://www.unavco.org/software/data-processing/teqc/teqc.html): a software for pre-processing GPS, GLONASS, Galileo, SBAS, Beidou, QZSS, and IRNSS data.
* [Crx2Rnx](https://terras.gsi.go.jp/ja/crx2rnx.html): software for compression/restoration of RINEX observation files.
