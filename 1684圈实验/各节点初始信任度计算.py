import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import scipy
import random
from scipy.stats import pearsonr


#jaccard相似系数:交集/并集
def correlation(a,b):
    unions = len(set(a).union(set(b)))
    intersections = len(set(a).intersection(set(b)))
    return 1. * intersections / unions

f = '节点信任值计算.txt'
fn = open(f, 'w')

attrbutes = np.loadtxt('1684.feat', delimiter=' ')
attrbutes1 = np.delete(attrbutes, [0] , axis = 1)
at_node_name = np.loadtxt('1684.feat' , usecols=(0,) , dtype=str)


ls_name = ['2849', '3021', '2694', '3096', '2818', '2725', '2951', '3285', '3082', '2832', '2960', '2800', '2929', '3029', '2909', '2880', '2754', '2872', '3232', '3184', '2948', '3277', '3297', '2925', '3397', '2939', '3185', '3115', '2927', '3426', '3333', '3394', '3087', '3236', '3327', '2675', '2863', '3296', '3293', '3384', '3005', '3039', '3428', '3139', '3198', '3417', '2944', '2738', '3399', '2777', '2894', '3320', '2793', '2787', '3377', '2778', '3101', '3214', '3090', '2729', '3085', '2966', '3033', '2919', '2893', '2771', '2749', '2986', '2829', '2711', '2755', '3149', '2887', '3247', '3347', '3065', '3286', '3419', '3319', '3046', '2773', '2666', '2706', '2940', '2852', '3226', '3316', '3050', '2667', '3117', '3173', '2913', '2676', '2878', '3249', '2897', '3119', '3204', '3351', '2801', '3256', '3191', '3203', '2846', '3321', '3124', '2803', '3280', '3132', '3207', '3042', '2963', '2987', '2946', '3335', '2697', '3292', '3026', '2786', '3170', '2875', '3047', '3108', '2750', '2908', '3412', '3056', '3025', '2679', '2756', '3098', '2906', '3120', '2916', '2680', '2742', '3350', '2716', '3051', '3240', '3331', '1405', '2905', '3145', '3045', '2789', '3182', '3434', '3420', '2730', '3106', '3307', '2847', '3396', '2936', '3361', '2764', '3018', '3248', '2856', '3156', '2843', '2945', '3257', '3263', '3057', '2888', '3287', '2840', '2731', '2821', '2985', '2698', '3360', '2989', '2683', '3301', '2907', '2928', '3385', '2795', '3239', '2661', '2910', '3233', '3244', '3391', '3049', '3392', '3193', '3054', '2690', '2844', '3252', '3355', '2718', '3136', '3152', '3366', '3346', '2904', '3150', '3102', '3169', '3178', '3208', '3267', '3116', '3386', '2665', '3332', '3243', '2886', '2999', '2708', '3016', '3342', '3022', '3306', '3298', '3411', '2833', '2994', '3416', '3064', '2689', '3104', '3364', '3302', '3291', '2783', '2734', '2828', '3353', '3035', '3043', '2871', '2739', '3324', '3339', '3345', '3299', '2757', '3288', '3234', '2992', '2854', '2724', '3425', '3402', '2920', '3095', '2877', '3060', '2782', '3000', '3174', '3094', '2765', '2869', '2991', '3078', '2717', '3225', '3024', '3231', '2943', '3009', '2901', '3107', '3343', '3253', '3086', '2688', '3068', '3415', '3406', '2794', '3073', '3374', '2964', '2715', '2865', '2748', '3215', '2978', '3430', '3077', '2968', '3167', '3040', '2918', '2890', '2892', '3074', '3127', '3289', '2955', '2813', '2827', '3118', '3019', '3380', '2780', '3262', '2772', '2835', '2763', '2662', '3206', '3176', '3201', '3114', '2726', '2953', '3330', '3137', '3328', '3144', '3369', '3079', '2719', '3403', '3044', '3273', '2728', '2864', '3387', '3237', '3014', '3219', '3076', '2720', '3344', '3348', '2741', '2839', '2810', '2911', '3414', '3259', '3189', '2745', '2853', '3158', '3123', '3295', '3001', '3075', '2921', '2820', '2896', '2988', '2873', '2702', '2874', '3013', '2687', '3099', '3242', '3138', '3162', '2923', '2677', '3379', '2759', '3278', '1534', '2851', '2938', '3113', '3378', '2866', '2760', '2790', '2867', '2834', '3423', '2891', '2870', '3246', '2912', '2956', '3241', '3363', '3315', '3017', '3172', '3112', '2883', '2669', '2831', '3326', '2781', '3129', '3362', '3223', '2996', '3341', '2997', '2933', '2973', '3212', '2950', '3111', '1758', '3218', '3053', '2758', '2672', '3261', '3318', '2700', '3100', '2815', '3266', '3398', '3435', '3222', '2751', '3192', '3422', '3069', '3258', '2937', '2733', '2696', '2830', '3154', '2753', '2796', '2931', '2682', '3313', '3227', '2674', '3032', '3352', '3188', '3337', '3356', '1450', '3166', '3312', '3160', '1642', '2993', '2806', '3213', '2770', '2848', '3004', '3300', '3059', '2969', '3135', '3146', '2862', '3070', '2915', '3180', '2732', '3365', '3400', '2819', '3309', '2879', '3418', '2967', '3092', '2673', '2785', '3027', '3171', '2841', '2962', '2934', '3023', '3433', '3195', '2816', '3220', '2974', '3228', '2735', '2709', '3002', '2965', '3390', '3084', '1505', '3245', '3010', '1666', '3080', '2712', '3373', '3265', '3164', '3151', '3421', '3148', '3284', '3370', '3093', '3041', '107', '1726', '2681', '2746', '3142', '3008', '2958', '3130', '3393', '2707', '3036', '3272', '2932', '3255', '2850', '3181', '3179', '3052', '3034', '3323', '3274', '3264', '3196', '2930', '3011', '3097', '3177', '2941', '2664', '2855', '3072', '2959', '3325', '3254', '990', '3216', '3141', '3304', '3381', '2685', '3109', '2668', '3140', '2723', '2836', '3367', '2976', '2686', '3168', '3405', '2900', '3413', '3187', '3081', '3283', '3165', '2768', '2701', '2727', '2982', '2693', '2984', '2980', '2699', '2703', '3089', '2797', '2917', '3235', '3224', '2845', '3186', '2809', '3388', '3003', '171', '2825', '2762', '3275', '2924', '3221', '2990', '3279', '3303', '3250', '3431', '3329', '3368', '3359', '3103', '3038', '3200', '3122', '3276', '3147', '2774', '2791', '3083', '2983', '3404', '2861', '3354', '2949', '3194', '3311', '3382', '2737', '2775', '3055', '2817', '2881', '2977', '3062', '3395', '3260', '2957', '2914', '2889', '3349', '2979', '3209', '3371', '2961', '3294', '2882', '2823', '2752', '2705', '3429', '3157', '3199', '3205', '3163', '3211', '2710', '2970', '2769', '3217', '2868', '3401', '3317', '2744', '3066', '3336', '3210', '3238', '3161', '3058', '2684', '2678', '2972', '2826', '1171', '3383', '3133', '3159', '3020', '2895', '2885', '3061', '2663', '3015', '2766', '3048', '3229', '2743', '2981', '3007', '2779', '3202', '2859', '2671', '2721', '3357', '2784', '3121', '2808', '2837', '3030', '3334', '3110', '3410', '2822', '3128', '2935', '2903', '2952', '1656', '2824', '3314', '2858', '3067', '2670', '2799', '2898', '3155', '2761', '2812', '3376', '2902', '3088', '2954', '3389', '3126', '2899', '2713', '2942', '2692', '2767', '2807', '2947', '2876', '3358', '3281', '2995', '1419', '2747', '2926', '3340', '3251', '3105', '2971', '3012', '3424', '3197', '3372', '3131', '3409', '3269', '58', '3290', '3427', '3153', '3432', '2804', '2811', '2736', '2805', '2695', '3143', '3175', '3310', '3125', '3028', '3308', '3190', '3091', '3305', '2798', '2922', '3408', '2838', '2740', '3338', '2802', '3063', '3436', '2884', '3322', '2722', '2714', '3282', '2814', '3270', '2776', '2975', '3006', '2860', '3037', '2691', '2792', '2998', '3268', '3407', '3271', '2857', '3375', '2788', '2704', '3134']

with open('邻居节点汇总.txt', 'r') as f:
    my_data = f.readlines() #txt中所有字符串读入data，得到的是一个list
    # 对list中的数据做分隔和类型转换
#    print(my_data)
#    for line in my_data:
#       line_data = line.split()
#       print (line_data)
print(len(my_data))

for i in range(len(ls_name)):
    i_node_name = int(ls_name[i])
    sum = 0
    line_data1 = my_data[i].split()
    for n in range(len(at_node_name)):
        if at_node_name[n] == ls_name[i]:
            at1 = attrbutes1[n]


    for nbr in line_data1:
        nbr_node_name = int(nbr)
        for m in range(len(at_node_name)):
            if at_node_name[m] == nbr:
                at2 = attrbutes1[m]
        s1 = pearsonr(at1, at2)[0]
        for j in range(len(ls_name)):
            if nbr == ls_name[j]:
                line_data2 = my_data[j].split()
                s2 = correlation(line_data1, line_data2)
        sum = sum + s1/2 + s2/2
    p_sum = sum/len(line_data1)
    fn.write(str(i_node_name) + ' ' + str(p_sum))
    fn.write('\n')
fn.close()




'''
i = 0
for node_name in ngr_node_name:
    i_node_name = int(node_name)
    sum = 0
    for nbr in ngr1[i]:
        nbr_node_name = int(nbr)
        s1 = pearsonr(attrbutes1[i_node_name - 1],attrbutes1[nbr_node_name - 1])[0]
        for j in len(ngr_node_name):
            if ngr_node_name[j] == nbr:
                s2 = correlation(ngr1[i], ngr1[j])
        sum = sum + s1 + s2
    sum = sum/len(ngr1[i])
    fn.write(node_name + ' ' + str(sum))
    fn.write('\n')
    i = i + 1
fn.close()
'''
