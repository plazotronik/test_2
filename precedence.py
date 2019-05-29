a=2.3;b=3;c=8
print('\nDefault Order:\t',a,'*',c,'+',b,'=',a*c+b,
        '\nForced Order:\t',a,'* (',c,'+',b,') =',a*(c+b),
            '\nDefault Order2:\t',b,'+',a,'*',c,'=',b+a*c)
print('\nDefault Order:\t',c,'/',b,'-',a,'=',c/b-a,
        '\nForced Order:\t',c,'/ (',b,'-',a,') =',c/(b-a),
            '\nDefault Order2:\t',-a,'+',c,'/',b,'=',-a+c/b)
print('\nDefault Order:\t',c,'%',a,'+',b,'=',c%a+b,
        '\nForced Order:\t',c,'% (',a,'+',b,') =',c%(a+b),
            '\nDefault Order2:\t',b,'+',c,'%',a,'=',b+c%a)
print('\nDefault Order:\t',c,'**',a,'+',b,'=',c**a+b,
        '\nForced Order:\t',c,'** (',a,'+',b,') =',c**(a+b),
              '\nDefault Order2:\t',b,'+',c,'**',a,'=',b+c**a)


