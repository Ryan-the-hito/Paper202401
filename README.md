# Paper202401

Data and commands used in State for Paper202401.

## 描述性统计

outreg2 using "/Users/ryanshenefield/Downloads/my_stats.docx", replace sum(log) title("Descriptive Statistics") tex

## 相关性分析（检测多重共线性）

pwcorr_a y_happen x_distance x_territory x_trade x_expect x_common x_fragile

## 多重共线性分析（VIF）

quietly reg y_happen x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect

estat vif

## 多重共线性分析

estat vif

## 单位根检验

xtunitroot fisher x_trade_cha, trend dfuller demean lags(1)【Fisher-ADF 检验】

xtunitroot llc x_trade_cha, trend demean lags(bic 1)【LLC 检验】

xtunitroot ips D_x_trade_cha, trend demean【IPS 检验】

## 一阶差分

gen D_x_trade_cha = d.x_trade_cha

## 协整分析

xtcointtest westerlund y_strong x_trade_cha , trend

xtcointtest westerlund y_happen x_trade_cha , trend

xtcointtest kao y_strong x_trade_cha, demean

xtcointtest kao y_happen x_trade_cha, demean

## 全文主回归

reg y_happen x_distance x_territory x_trade_cha x_expect x_common x_fragile

est store OLS_ter1

reg y_strong x_distance x_territory x_trade_cha x_expect x_common x_fragile

est store OLS_ter2

esttab OLS_ter1 OLS_ter2, style(tex) label booktabs replace

## Logit 回归

logit y_happen x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect, or /*总回归*/

est store m0

logit y_happen  x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect, or /*去掉距离因素*/

est store m1

logit y_happen x_distance x_trade_cha x_expect x_common x_fragile trade_cha_expect, or /*去掉接壤因素*/

est store m2

logit y_happen x_distance x_territory x_expect x_common x_fragile trade_cha_expect, or /*去掉贸易因素*/

est store m3

logit y_happen x_distance x_territory x_trade_cha x_common x_fragile trade_cha_expect, or /*去掉期望值因素*/

est store m4

logit y_happen x_distance x_territory x_trade_cha x_expect x_fragile trade_cha_expect, or /*去掉协同性因素*/

est store m5

logit y_happen x_distance x_territory x_trade_cha x_expect x_common trade_cha_expect, or /*去掉脆弱性*/

est store m6

logit y_happen x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_distance > 1466 , or/*条件：距离大于平均距离*/

est store m7

logit y_happen x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_distance < 1466 , or/*条件：距离小于平均距离*/

est store m8

logit y_happen x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_territory == 1, or /*条件：有接壤*/

est store m9

logit y_happen x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_territory == 0, or /*条件：无接壤*/

est store m10

logit y_happen x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_territory == 0 & x_distance < 1466, or /*条件：距离小于平均距离且无接壤（中间地带）*/

est store m11

logit y_happen x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_common >= 1 , or/*条件：与被制裁国有共同性*/

est store m12

logit y_happen x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_common == 0 , or/*条件：与被制裁国无共同性*/

est store m13

logit y_happen x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_fragile < 0.815 , or/*条件：国家更坚强*/

est store m14

logit y_happen x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_fragile > 0.815 , or/*条件：国家更脆弱*/

est store m15

esttab m0 m1 m2 m3 m4 m5 m6 m7, b se mtitle

esttab m8 m9 m10 m11 m12 m13 m14 m15, b se mtitle

coefplot m0 m1 m2 m3 m4 m5 m6 m7, drop(_cons) xline(0)

coefplot m8 m9 m10 m11 m12 m13 m14 m15, drop(_cons) xline(0)

esttab m0 m1 m2 m3 m4 m5 m6 m7, b se mtitle eform

esttab m8 m9 m10 m11 m12 m13 m14 m15, b se mtitle eform

esttab m0 m1 m2 m3 m4 m5 m6 m7, style(tex) label booktabs replace

esttab m8 m9 m10 m11 m12 m13 m14 m15, style(tex) label booktabs replace

esttab m0 m1 m2 m3 m4 m5 m6 m7, style(tex) label booktabs replace eform

esttab m8 m9 m10 m11 m12 m13 m14 m15, style(tex) label booktabs replace eform

margins, dydx(*)/*边际效应*/

## 稳健性检验（Logit）

*estat gof/*拟合优度检验，非稳健性检验*/

bootstrap, reps(1000): logit y_happen x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect/*抽样 1000 次*/

est store t0

logit y_happen x_distance x_territory x_trade_cha x_expect x_culture_lan x_culture_peo x_culture_rel x_fragile trade_cha_expect, or /*变为三分项*/

est store t1

logit y_happen x_distance x_territory x_trade_cha x_expect x_culture_lan x_fragile trade_cha_expect, or /*仅语言*/

est store t2

logit y_happen x_distance x_territory x_trade_cha x_expect x_culture_peo x_fragile trade_cha_expect, or /*仅民族*/

est store t3

logit y_happen x_distance x_territory x_trade_cha x_expect x_culture_rel x_fragile trade_cha_expect, or /*仅宗教*/

est store t4

logit y_happen x_distance x_territory x_trade_cha x_expect x_common x_polity trade_cha_expect, or /*政体 5*/

est store t5

logit y_happen x_distance x_territory x_trade_cha x_expect x_common x_democracy trade_cha_expect, or /*民主指数*/

est store t6

logit y_happen x_territory x_trade_cha x_expect x_distance_r x_common x_fragile trade_cha_expect, or /*距离因素俄罗斯*/

est store t7

esttab t0 t1 t2 t3 t4 t5 t6 t7, style(tex) label booktabs replace eform

## OLS 回归

reg y_strong x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect /*总回归*/

est store m16

reg y_strong x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect /*去掉距离因素*/

est store m17

reg y_strong x_distance x_trade_cha x_expect x_common x_fragile trade_cha_expect  /*去掉接壤因素*/

est store m18

reg y_strong x_distance x_territory x_expect x_common x_fragile trade_cha_expect /*去掉贸易因素*/

est store m19

reg y_strong x_distance x_territory x_trade_cha x_common x_fragile trade_cha_expect /*去掉期望值因素*/

est store m20

reg y_strong x_distance x_territory x_trade_cha x_expect x_fragile trade_cha_expect /*去掉协同性因素*/

est store m21

reg y_strong x_distance x_territory x_trade_cha x_expect x_common trade_cha_expect /*去掉脆弱性*/

est store m22

reg y_strong x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_distance > 1466 /*条件：距离大于平均距离*/

est store m23

reg y_strong x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_distance < 1466 /*条件：距离小于平均距离*/

est store m24

reg y_strong x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_territory == 1/*条件：有接壤*/

est store m25

reg y_strong x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_territory == 0/*条件：无接壤*/

est store m26

reg y_strong x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_territory == 0 & x_distance < 1466 /*条件：距离小于平均距离且无接壤（中间地带）*/

est store m27

reg y_strong x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_common == 1 /*条件：与被制裁国有共同性*/

est store m28

reg y_strong x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_common == 0 /*条件：与被制裁国无共同性*/

est store m29

reg y_strong x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_fragile < 0.815 /*条件：国家更坚强*/

est store m30

reg y_strong x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_fragile > 0.815 /*条件：国家更脆弱*/

est store m31

esttab m16 m17 m18 m19 m20 m21 m22 m23, b se mtitle

esttab m24 m25 m26 m27 m28 m29 m30 m31, b se mtitle

coefplot m16 m17 m18 m19 m20 m21 m22 m23, drop(_cons) xline(0)

*coefplot m24 m25 m26 m27 m28 m29 m30 m31, drop(_cons) xline(0)

esttab m16 m17 m18 m19 m20 m21 m22 m23, style(tex) label booktabs replace

esttab m24 m25 m26 m27 m28 m29 m30 m31, style(tex) label booktabs replace

## OLS 异方差检验

reg y_strong x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect /*总回归*/

estat imtest, white

reg y_strong x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect /*去掉距离因素*/

estat imtest, white

reg y_strong x_distance x_trade_cha x_expect x_common x_fragile trade_cha_expect  /*去掉接壤因素*/

estat imtest, white

reg y_strong x_distance x_territory x_expect x_common x_fragile trade_cha_expect /*去掉贸易因素*/

estat imtest, white

reg y_strong x_distance x_territory x_trade_cha x_common x_fragile trade_cha_expect /*去掉期望值因素*/

estat imtest, white

reg y_strong x_distance x_territory x_trade_cha x_expect x_fragile trade_cha_expect /*去掉协同性因素*/

estat imtest, white

reg y_strong x_distance x_territory x_trade_cha x_expect x_common trade_cha_expect /*去掉脆弱性*/

estat imtest, white

reg y_strong x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_distance > 1466 /*条件：距离大于平均距离*/

estat imtest, white

reg y_strong x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_distance < 1466 /*条件：距离小于平均距离*/

estat imtest, white

reg y_strong x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_territory == 1/*条件：有接壤*/

estat imtest, white

reg y_strong x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_territory == 0/*条件：无接壤*/

estat imtest, white

reg y_strong x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_territory == 0 & x_distance < 1466 /*条件：距离小于平均距离且无接壤（中间地带）*/

estat imtest, white

reg y_strong x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_common >= 1 /*条件：与被制裁国有共同性*/

estat imtest, white

reg y_strong x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_common == 0 /*条件：与被制裁国无共同性*/

estat imtest, white

reg y_strong x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_fragile < 0.815 /*条件：国家更坚强*/

estat imtest, white

reg y_strong x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_fragile > 0.815 /*条件：国家更脆弱*/

estat imtest, white

reg y_strong x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect, vce(robust) /*总回归*/

est store t8

reg y_strong x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect, vce(robust) /*去掉距离因素*/

est store t9

reg y_strong x_distance x_trade_cha x_expect x_common x_fragile trade_cha_expect, vce(robust)  /*去掉接壤因素*/

est store t10

reg y_strong x_distance x_territory x_expect x_common x_fragile trade_cha_expect, vce(robust) /*去掉贸易因素*/

est store t11

reg y_strong x_distance x_territory x_trade_cha x_common x_fragile trade_cha_expect, vce(robust) /*去掉期望值因素*/

est store t12

reg y_strong x_distance x_territory x_trade_cha x_expect x_fragile trade_cha_expect, vce(robust) /*去掉协同性因素*/

est store t13

reg y_strong x_distance x_territory x_trade_cha x_expect x_common trade_cha_expect, vce(robust) /*去掉脆弱性*/

est store t14

reg y_strong x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_distance > 1466, vce(robust) /*条件：距离大于平均距离*/

est store t15

reg y_strong x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_distance < 1466, vce(robust) /*条件：距离小于平均距离*/

est store t16

reg y_strong x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_territory == 1, vce(robust)/*条件：有接壤*/

est store t17

reg y_strong x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_territory == 0, vce(robust)/*条件：无接壤*/

est store t18

reg y_strong x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_territory == 0 & x_distance < 1466, vce(robust) /*条件：距离小于平均距离且无接壤（中间地带）*/

est store t19

reg y_strong x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_common == 1, vce(robust)/*条件：与被制裁国有共同性*/

est store t20

reg y_strong x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_common == 0, vce(robust)/*条件：与被制裁国无共同性*/

est store t21

reg y_strong x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_fragile < 0.815, vce(robust) /*条件：国家更坚强*/

est store t22

reg y_strong x_distance x_territory x_trade_cha x_expect x_common x_fragile trade_cha_expect if x_fragile > 0.815, vce(robust)/*条件：国家更脆弱*/

est store t23

esttab t8 t9 t10 t11 t12 t13 t14 t15, style(tex) label booktabs replace

esttab t16 t17 t18 t19 t20 t21 t22 t23, style(tex) label booktabs replace

## OLS 稳健性检验

reg y_strong_acu x_distance x_territory x_trade x_common x_fragile, vce(robust) /*换 acu 因变量*/

est store t24

reg y_strong x_distance x_territory x_trade_cha x_expect x_culture_lan x_culture_peo x_culture_rel x_fragile trade_cha_expect, vce(robust) /*变为三分项*/

est store t25

reg y_strong x_distance x_territory x_trade_cha x_expect x_culture_lan x_fragile trade_cha_expect, vce(robust) /*仅语言*/

est store t26

reg y_strong x_distance x_territory x_trade_cha x_expect x_culture_peo x_fragile trade_cha_expect, vce(robust) /*仅民族*/

est store t27

reg y_strong x_distance x_territory x_trade_cha x_expect x_culture_rel x_fragile trade_cha_expect, vce(robust) /*仅宗教*/

est store t28

reg y_strong x_distance x_territory x_trade_cha x_expect x_common x_polity trade_cha_expect, vce(robust) /*政体 5*/

est store t29

reg y_strong x_distance x_territory x_trade_cha x_expect x_common x_democracy trade_cha_expect, vce(robust) /*民主指数*/

est store t30

reg y_strong x_territory x_trade_cha x_expect x_distance_r x_common x_fragile trade_cha_expect, vce(robust) /*距离因素俄罗斯*/

est store t31

esttab t24 t25 t26 t27, style(tex) label booktabs replace

esttab t28 t29 t30 t31, style(tex) label booktabs replace