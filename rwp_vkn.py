import matplotlib.pyplot as plt

#rwp
import numpy as np
#
step = [ 16 , 20,  24,  28,  32,  36,  40,  44,  48,  52 , 56,  60,  64,  68,  72,  76,  80,  84,
  88,  92,  96 ,100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140, 144, 148, 152, 156,
 160, 164, 168, 172, 176, 180, 184, 188, 192, 196, 200, 204, 208, 212, 216, 220]
vkn_noise_0_acc = np.array([0.41632035, 0.49294372, 0.56727273, 0.61,       0.6517316,  0.66848485,
 0.68844156, 0.70441558, 0.72311688, 0.73471862, 0.74190476, 0.74731602,
 0.75151515, 0.75393939, 0.7630303 , 0.76380953, 0.76891775, 0.77095238,
 0.77380952, 0.77467533, 0.78393939, 0.7825974 , 0.78316018, 0.78839827,
 0.78649351, 0.78727273, 0.79134199, 0.79484849, 0.79714286, 0.79896104,
 0.79896104, 0.80034632, 0.80523809, 0.80532468, 0.80805195, 0.81168831,
 0.81181818, 0.8147619 , 0.81316017, 0.81225108, 0.81329005, 0.80774892,
 0.80584415, 0.80787879, 0.80917749, 0.81242424, 0.81900433, 0.82324675,
 0.82385281, 0.82264069, 0.82294373, 0.82264069])
vkn_noise_0_error =np.array( [0.03247661, 0.03170097, 0.02558809, 0.02136526, 0.01753221, 0.01477298,
 0.01475358, 0.0132202 , 0.0103993,  0.00962253, 0.01082505, 0.00983929,
 0.0093871,  0.00815473, 0.00671953, 0.00696388, 0.00703173, 0.00862837,
 0.00577296, 0.0088332 , 0.00640665, 0.00622614, 0.00611857, 0.00528666,
 0.0068221 , 0.00718094, 0.00444252, 0.0060856 , 0.00581361, 0.00726812,
 0.00792517, 0.00680413, 0.00603001, 0.00530957, 0.00640238, 0.00523875,
 0.00564688, 0.00558297, 0.00679026, 0.00692913, 0.00738367, 0.00784516,
 0.00696209, 0.00710674, 0.00912109, 0.00749435, 0.00468951, 0.00447528,
 0.00471972, 0.00502496, 0.00551233, 0.00536692])
vkn_noise_0_loss = np.array([2.26316881, 1.93096337, 1.70338016, 1.53360119, 1.38737156, 1.2851844,
 1.19416608, 1.11446493, 1.05338561, 1.00841918, 0.95890007, 0.91810544,
 0.88905497, 0.86471102, 0.84819489, 0.82983004, 0.80478296, 0.78786573,
 0.77803101, 0.76299258, 0.75233656, 0.73697357, 0.73048344, 0.71592738,
 0.71053613, 0.69904044, 0.69263029, 0.68475938, 0.67939926, 0.67171958,
 0.66664567, 0.64855398, 0.64775006, 0.64610833, 0.63520505, 0.63164295,
 0.62806418, 0.62214545, 0.61845575, 0.60875312, 0.61285993, 0.61102727,
 0.6053215 , 0.60622386, 0.61486644, 0.60838998, 0.60305297, 0.59241601,
 0.57826075, 0.57838005, 0.57526221, 0.56916315])
vkn_noise_0_lerror = np.array([0.03793615, 0.02527534, 0.0320589,  0.02301387, 0.02443354, 0.02713488,
 0.02753839, 0.02097901, 0.01904055, 0.01934981, 0.01781967, 0.01719826,
 0.01511376, 0.01819002, 0.01765609, 0.01498023, 0.01136129, 0.01061173,
 0.01455086, 0.01227008, 0.01291331, 0.0130483 , 0.01235061, 0.01014231,
 0.01116849, 0.01253789, 0.01326867, 0.01058777, 0.01384705, 0.01540128,
 0.0177118 , 0.01262039, 0.01077535, 0.01152438, 0.01189131, 0.01130371,
 0.0142579 , 0.01345339, 0.01394515, 0.01297293, 0.01743782, 0.01759241,
 0.01430541, 0.01489566, 0.0210101 , 0.01686494, 0.01499842, 0.01160242,
 0.00998324, 0.00871263, 0.00811149, 0.00745362])
#f
vkn_noise_05_acc = np.array([0.24675325, 0.29445887, 0.37930736, 0.44017316, 0.51484848 ,0.56004329,
 0.59298701, 0.61372294, 0.64116884, 0.65692641, 0.66493507, 0.68735931,
 0.70008658 ,0.70376624, 0.71025974, 0.72450216, 0.73060606, 0.73670996,
 0.73506494 ,0.73367965, 0.7435065 , 0.74874459, 0.75164502, 0.75528138,
 0.7595671 , 0.76584416, 0.76402598, 0.76727273, 0.77004329, 0.76904762,
 0.77519481, 0.77333333, 0.77627705, 0.78004329, 0.78177489, 0.77653679,
 0.77766234, 0.78069264, 0.78506493, 0.78333333, 0.78839827, 0.78887446,
 0.7904329 , 0.79203463, 0.795671  , 0.79385281, 0.79753247, 0.79670996,
 0.79709091, 0.79935065, 0.79878788, 0.79874459])
vkn_noise_05_error = np.array([0.02115726, 0.02084931, 0.03031229, 0.02281471, 0.0184554,  0.02124085,
 0.01679122, 0.01660163, 0.01341469, 0.01237154, 0.01281863, 0.01114172,
 0.0108534 , 0.00858813, 0.01023013, 0.00878236, 0.00781097, 0.00906505,
 0.00908342, 0.00903207, 0.00722717, 0.00778837, 0.00763126, 0.00698038,
 0.00635593, 0.00793455, 0.00755014, 0.00724265, 0.0082991 , 0.00878418,
 0.00914611, 0.00927465, 0.00611378, 0.00684511, 0.00716097, 0.00826675,
 0.0070511 , 0.00666348, 0.00569765, 0.0059022 , 0.00604508, 0.0050267,
 0.00585466, 0.00647523, 0.00526581, 0.00585114, 0.00516086, 0.00593976,
 0.00620707, 0.00580695, 0.00527921, 0.0053231 ])
vkn_noise_05_loss =np.array([2.27500579, 2.19214483, 2.08318665, 1.97122834, 1.77329931, 1.62550368,
 1.48915245, 1.37767697, 1.28561257, 1.22295646, 1.16366068, 1.11757613,
 1.07824569, 1.03772314, 0.99205567, 0.97042033, 0.93458936, 0.90384057,
 0.89031676, 0.87478783, 0.87398418, 0.85288655, 0.82830264, 0.81584034,
 0.80811618, 0.79193686, 0.78560879, 0.77234721, 0.7715621 , 0.75551057,
 0.75084711, 0.73424551, 0.72997304, 0.73289565, 0.72459253, 0.71911671,
 0.69857864, 0.71172269, 0.7046849 , 0.69581264, 0.69264757, 0.68712959,
 0.68868742, 0.68427272, 0.67116541, 0.6628434,  0.66252809, 0.66103265,
 0.65784258, 0.64715527, 0.64081508, 0.63889458])
vkn_noise_05_lerror = np.array([0.00879558, 0.01638274, 0.01918605, 0.02871129 ,0.02544945, 0.02422369,
 0.0216911 , 0.02152452, 0.02301459, 0.02290712, 0.02263061, 0.01983321,
 0.01776785, 0.01789136, 0.01889929, 0.01636818, 0.01353346, 0.01301541,
 0.01090355, 0.01380701, 0.01551461, 0.01279235, 0.01116888, 0.012534,
 0.01092104, 0.01041226, 0.01215238, 0.01117919, 0.01360478, 0.01310819,
 0.01641173, 0.01643235, 0.01744531, 0.01635877, 0.01380315, 0.01602499,
 0.01198328, 0.01434533, 0.01692543, 0.01257738, 0.01118799, 0.01246539,
 0.01230155, 0.01405368, 0.01278305 ,0.01296373, 0.01514497, 0.01685457,
 0.01556137, 0.01137139, 0.01360368, 0.0125767 ])
#
vkn_noise_075_acc = np.array([0.18839827, 0.20645022, 0.24497835, 0.28194805, 0.34367966, 0.38484848,
 0.42584416, 0.45376623, 0.48095238, 0.50190476, 0.53926407, 0.54822511,
 0.56199134, 0.60160173, 0.60207792, 0.62017316, 0.61705628, 0.63493507,
 0.64272728, 0.64874459, 0.66281385, 0.66194806, 0.66099567, 0.67090909,
 0.67688312, 0.67359308, 0.67878788, 0.68593074, 0.6869697 , 0.69666667,
 0.70515152, 0.69995671, 0.70506494, 0.70948052, 0.71653679, 0.71831169,
 0.71588744, 0.71467532, 0.72134199, 0.71861472, 0.71982684, 0.7247619,
 0.72      , 0.71965368, 0.71857143, 0.72359307, 0.73385281, 0.73450216,
 0.73510823, 0.74476191, 0.74164502, 0.74541126])
vkn_noise_075_error = np.array([0.01355328, 0.01250004, 0.01703172, 0.02241794, 0.02000087, 0.02231549,
 0.01957429, 0.01608467, 0.01625759, 0.01845533, 0.01738834, 0.01354245,
 0.02028515, 0.01093519, 0.01150499, 0.00786924, 0.01248665, 0.00880141,
 0.01028014, 0.0114126 , 0.01229934, 0.00890279, 0.0112253 , 0.00892674,
 0.01195629, 0.01012403, 0.01428198, 0.00912964, 0.00924998, 0.00969454,
 0.00893907, 0.00779721, 0.00992614, 0.00745218, 0.00944338, 0.01002882,
 0.01048434, 0.01040098, 0.00962299, 0.01004216, 0.00992845, 0.00696266,
 0.00763871, 0.00922584, 0.00886686, 0.00759455, 0.00950915, 0.00803985,
 0.00654878, 0.00771148, 0.00928493, 0.00947191])
vkn_noise_075_loss = np.array([2.32826844, 2.31330196, 2.31519332, 2.35933874, 2.23122135, 2.12054566,
 1.8868803 , 1.77746124, 1.68278765 ,1.58123501, 1.49657811, 1.45567786,
 1.40077951, 1.3291405 , 1.28424169 ,1.17604644, 1.16591442, 1.14520924,
 1.14442731, 1.0992867 , 1.08885561, 1.0650316 , 1.04871851, 1.0354652,
 1.00683845, 0.99158265, 0.97725973, 0.97735851, 0.98824828, 0.96287151,
 0.9422812 , 0.92544901, 0.91803713, 0.90881848, 0.89979286, 0.88993664,
 0.87041371, 0.87402917, 0.88271214, 0.85970093, 0.87155862, 0.86216841,
 0.85684175, 0.85622951, 0.86816307, 0.86632967, 0.8376081 , 0.85635135,
 0.834095  , 0.82044395, 0.83112408, 0.82232029])
vkn_noise_075_lerror = np.array([0.01128082, 0.02159968, 0.04299914, 0.0632999,  0.05171285, 0.07002179,
 0.03843663 ,0.06321428, 0.04759095, 0.05593921, 0.05100968, 0.0449401,
 0.05126988, 0.03673259, 0.03199536, 0.0198605 , 0.02680601, 0.02118612,
 0.02940787, 0.02484349, 0.02834235, 0.02849696, 0.02515602, 0.02755605,
 0.02557721, 0.02070865, 0.02365468, 0.03202931, 0.03499083, 0.03429716,
 0.02194838, 0.02188889, 0.02355505, 0.02700978, 0.02312532, 0.02219137,
 0.02385467, 0.02562834, 0.02845074, 0.02397025, 0.02769039, 0.02331581,
 0.02302676, 0.02263948, 0.02349256, 0.02759046, 0.02183092, 0.01974505,
 0.02155565, 0.02078697, 0.02320461, 0.02429502])




#accuracy
#noise 0
plt.title('Model Accuracy per training step- RWP')
plt.fill_between(step, vkn_noise_0_acc - vkn_noise_0_error,  vkn_noise_0_acc + vkn_noise_0_error, color='blue', alpha=0.3)
plt.plot(
        step,
        vkn_noise_0_acc,
        color='blue',
        label="VKN+FL training - noise multiplier 0",
        linewidth=0.8)


#noise_05
plt.fill_between(
        step,
        vkn_noise_05_acc -
        vkn_noise_05_error,
        vkn_noise_05_acc +
        vkn_noise_05_error,
        color='orange',
        alpha=0.5)
plt.plot(
        step,
        vkn_noise_05_acc,
        color='red',
        label="VKN+FL training - noise multiplier 0.5",
        linewidth=0.8)


#noise_0.75
plt.fill_between(
        step,
        vkn_noise_075_acc -
        vkn_noise_075_error,
        vkn_noise_075_acc +
        vkn_noise_075_error,
        color='green',
        alpha=0.5)
plt.plot(
        step,
        vkn_noise_075_acc,
        color='green',
        label="VKN+FL training - noise multiplier 0.75",
        linewidth=0.8)

plt.xlabel("Training step")
plt.ylabel("Model accuracy ∈ [0;1]")
plt.legend()

plt.show()




#Loss

#noise 0
plt.title('Loss per training step -RWP')

plt.fill_between(step, vkn_noise_0_loss - vkn_noise_0_lerror, vkn_noise_0_loss + vkn_noise_0_lerror, color='blue', alpha=0.3)
plt.plot(
        step,
        vkn_noise_0_loss,
        color='blue',
        label="VKN+FL training - noise multiplier 0 ",
        linewidth=0.8)

#05_loss
plt.fill_between(
        step,
        vkn_noise_05_loss -
        vkn_noise_05_lerror,
        vkn_noise_05_loss +
        vkn_noise_05_lerror,
        color='orange',
        alpha=0.5)
plt.plot(
        step,
        vkn_noise_05_loss,
        color='red',
        label="VKN+FL training - noise multiplier 0.5",
        linewidth=0.8)

#075_loss
plt.fill_between(
        step,
        vkn_noise_075_loss -
        vkn_noise_075_lerror,
        vkn_noise_075_loss +
        vkn_noise_075_lerror,
        color='green',
        alpha=0.5)
plt.plot(
        step,
        vkn_noise_075_loss,
        color='green',
        label="VKN+FL training - noise multiplier 0.75",
        linewidth=0.8)

plt.xlabel("Training step")
plt.ylabel("Loss")
plt.legend()

plt.show()

