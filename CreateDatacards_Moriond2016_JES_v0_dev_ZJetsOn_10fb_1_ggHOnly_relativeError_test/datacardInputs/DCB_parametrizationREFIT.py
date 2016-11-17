#---

#         _\|/_
#         (o o)
# +----oOO-{_}-OOo-----------------------------------------------------------------+
# |Double Crystal-ball parameters expressed as a function of mH around mH : 125 GeV|
# +--------------------------------------------------------------------------------+
#
#setup: &setup
#    parametrization_name: 'Linear [120-130]'
#    color: 4

shape = {

#2e2mu_inclusive:
#    <<     : *setup
#    'mean_3' : '124.812245508+(0.992098516531)*(@0-125)',
#    'sigma_3' : '1.34318471467+(0.00446481560236)*(@0-125)',
#    'alpha_3' : '1.00699495654',
#    'n_3' : '2.82780783836+(-0.0224567979969)*(@0-125)',
#    'alpha2_3' : '1.40516505504',
#    'n2_3' : '4.3401062829+(0.0708733850487)*(@0-125)',
'mean_3' : '124.821982212+(0.993837981073)*(@0-125)',
'sigma_3' : '1.35114407214+(0.00509758180529)*(@0-125)',
'alpha_3' : '1.00241622948',
'n_3' : '2.85941829098+(-0.0221498368964)*(@0-125)',
'alpha2_3' : '1.39930810743',
'n2_3' : '4.4000909192+(0.0749747134711)*(@0-125)',

#4mu:
#    <<     : *setup

#    'mean_1' : '124.765108592+(0.993385375758)*(@0-125)',
#    'sigma_1' : '1.5432767678+(0.00656994459132)*(@0-125)',
#    'alpha_1' : '1.28661471089',
#    'n_1' : '1.9579637601+(-0.00601795782582)*(@0-125)',
#    'alpha2_1' : '1.89341469959',
#    'n2_1' : '2.7822938539+(0.0187407842516)*(@0-125)',
'mean_1' : '124.7+(0.99478298557)*(@0-125)',
'sigma_1' : '1.117e+(0.006953726512)*(@0-125)',
'alpha_1' : '1.273',
'n_1' : '2.022+(-0.00778345816166)*(@0-125)',
'alpha2_1' : '1.991',
'n2_1' : '2.682+(0.0162820864236)*(@0-125)',

#4e:
#    <<     : *setup

#    'mean_2' : '124.74906717+(0.988367966883)*(@0-125)',
#    'sigma_2' : '1.76135801645+(0.00163621431441)*(@0-125)',
#    'alpha_2' : '0.887911007092',
#    'n_2' : '4.26437487431+(-0.0529211812262)*(@0-125)',
#    'alpha2_2' : '1.30606463691',
#    'n2_2' : '6.2445291559+(0.247379341522)*(@0-125)'
'mean_2' : '124.748279815+(0.987967527032)*(@0-125)',
'sigma_2' : '1.75831564174+(0.00459176110223)*(@0-125)',
'alpha_2' : '0.89010933338',
'n_2' : '4.18131491186+(-0.0405013870048)*(@0-125)',
'alpha2_2' : '1.30590873434',
'n2_2' : '6.38563686832+(0.332333210419)*(@0-125)',


}
