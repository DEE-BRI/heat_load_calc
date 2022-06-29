.. include:: definition.txt

.. raw:: latex

    \clearpage

========================================================================================================================
湿気バランス
========================================================================================================================

------------------------------------------------------------------------------------------------------------------------
1. 室全体の水分収支
------------------------------------------------------------------------------------------------------------------------

室 |i| の空気の水分収支は式(1)で表される。

.. math::
    :nowrap:

    \begin{align*}
        \begin{split}
            \rho_a \cdot V_{room,i} \cdot \frac{dX_{r,i}}{dt}
            &= \rho_a \cdot V_{vent,out,i} \cdot ( X_o - X_{r,i} ) + G_{lh,frt,i} \cdot ( X_{frt,i} - X_{r,i} ) \\
            &+ \rho_a \cdot \sum_{j=0}^{J-1}{V_{vent,int,i,j} \cdot (X_{r,j} - X_{r,i})} + X_{gen,i} + X_{hum,i} + L_{L,i}
        \end{split}
        \tag{1}
    \end{align*}

ここで、

:math:`\rho_a` : 空気の密度, kg / |m3| 

:math:`V_{room,i}` : 室 |i| の容積, |m3| 

:math:`X_{r,i}` : 室 |i| の絶対湿度, kg / kg(DA)

:math:`X_{r,j}` : 室 |j| の絶対湿度, kg / kg(DA)

:math:`t` : 時間, s

:math:`V_{vent,out,i}` : 室 |i| の外気との換気量, |m3| /s

:math:`X_o` : 外気絶対湿度, kg/kg(DA)

:math:`G_{lh,frt,i}` : 室 |i| の備品等と空気間の湿気コンダクタンス, kg / (s kg/kg(DA))

:math:`X_{frt,i}` : 室 |i| の備品等の絶対湿度, kg / kg(DA)

:math:`V_{vent,int,i,j}` : 室 |j| から室 |i| への機械換気量, |m3| / s

:math:`X_{gen,i}` : 室 |i| の人体発湿を除く内部発湿, kg / s

:math:`X_{hum,i}` : 室 |i| の人体発湿, kg / s

:math:`L_{L,i}` : 室 |i| の潜熱負荷（加湿を正・除湿を負とする）, kg / s

である。

空調による除湿・加湿の方法として以下のパターンを想定する。

- 除湿・加湿を行わない場合
- （加湿器の使用など）固定値で除湿・加湿を行う場合
- 目標絶対湿度を満たすように除湿・加湿を行う場合（従来の負荷計算方法）
- 室内の絶対湿度に応じて除湿量が定まる場合（放射パネルやエアコンなど除湿量を完全には制御しない方式）

これらを踏まえて、一般的に室 |i| の潜熱負荷 :math:`L_{L,i}` を以下の式で表す。

.. math::
    :nowrap:

    \begin{align*}
        L_{L,i} = L_{a,i} \cdot X_{r,i} + L_{b,i} \tag{2}
    \end{align*}

除湿・加湿を行わない場合、 :math:`L_{a,i} = 0` 及び :math:`L_{b,i} = 0` とすればよい。

ある一定値で除加湿を行う場合、 :math:`L_{a,i} = 0` とし、与えたい除湿・加湿量を  :math:`L_{b,i}`  に与えれば良い。

目標絶対湿度を満たすように除湿・加湿を行う場合、 :math:`L_{a,i} = 0` とし、 :math:`X_{r,i}` を目標絶対湿度としたうえで、
:math:`L_{b,i}` を未知数として除湿・加湿量を求めれば良い。

室内の絶対湿度に応じて除湿を行う方法の場合、室内の絶対湿度と除湿を行う表面の飽和絶対湿度との差によって除湿量が決定される場合が多い。
その場合、以下のような式で表される。

.. math::
    :nowrap:

    \begin{align*}
        L_{L,i} = \begin{cases}
            -k_{l,i} \cdot (X_{r,i} - X_{srf,ex,i}) & ( X_{r,i} \gt X_{srf,ex,i} ) \\
            0 & ( X_{srf,ex,i} \le X_{r,i} )
        \end{cases}
        \tag{3}
    \end{align*}

ここで、

:math:`X_{srf,ex,i}` : 室 |i| に設置された設備の熱交換器表面の飽和絶対湿度, kg/kg(DA)

:math:`k_{l,i}` : 室 |i| に設置された設備の熱交換器表面の湿気コンダクタンス, kg/(s kg/kg(DA))

である。このように、絶対湿度と熱交換器表面における飽和絶対湿度との大小関係によって除湿の有無が決定されるため、
数値計算においては、一旦、除湿を行わない場合の絶対湿度 :math:`X_{r,ndh}` を求め、
その湿度と熱交換器表面における飽和絶対湿度 :math:`X_{srf,ex,i}` の大小を比較して除湿の有無を決定することになる。
なお、 :math:`L_{a,i}` 及び :math:`L_{b,i}` の決定方法は後述する。

備品等の水分収支式は室空気との物質移動だけを考慮すればよいため、次式で表すことができる。

.. math::
    :nowrap:

    \begin{align*}
    	C_{lh,frt,i} \cdot \frac{dX_{frt,i}}{dt} = G_{lh,frt,i} \cdot ( X_{r,i} - X_{frt,i} ) \tag{4}
    \end{align*}

ここで、

:math:`C_{lh,frt,i}` : 室 |i| の備品等の湿気容量, kg/(kg/kg(DA))

である。

式(2)を式(1)に代入して後退差分で離散化すると次式となる。

.. math::
    :nowrap:

    \begin{align*}
        \begin{split}
            \rho_a \cdot V_{room,i} \cdot \frac{ X_{r,i,n+1} - X_{r,i,n} }{ \Delta t }
            &= \rho_a \cdot \hat{V}_{vent,out,i,n} \cdot ( X_{o,n+1} - X_{r,i,n+1} ) \\
            &+ G_{lh,frt,i} \cdot ( X_{frt,i,n+1} - X_{r,i,n+1} ) \\
            &+ \rho_a \cdot \sum_{j=0}^{J-1}{\hat{V}_{vent,int,i,j,n} \cdot ( X_{r,j,n+1} - X_{r,i,n+1} ) } \\
            &+ \hat{X}_{gen,i,n} + \hat{X}_{hum,i,n} + \hat{L}_{a,i,n} \cdot X_{r,i,n+1} + \hat{L}_{b,i,n}
        \end{split}
    	\tag{5}
    \end{align*}

ここで、

:math:`\Delta t` : 1ステップの時間間隔, s

:math:`X_{r,i,n}` : ステップ |n| における室 |i| の絶対湿度, kg/kg(DA)

:math:`X_{r,j,n}` : ステップ |n| における室 |j| の絶対湿度, kg/kg(DA)

:math:`\hat{V}_{out,vent,i,n}` : ステップ |n| からステップ |n+1| における室 |i| の外気との換気量, |m3| /s

:math:`X_{o,n}` : ステップ |n| における外気絶対湿度, kg/kg(DA)

:math:`X_{frt,i,n}` : ステップ |n| における室 |i| の備品等の絶対湿度, kg/kg(DA)

:math:`\hat{V}_{int,vent,i,j,n}` : ステップ |n| からステップ |n+1| における室 |j| から室 |i| への機械換気量, |m3| /s

:math:`\hat{X}_{gen,i,n}` : ステップ |n| における室 |i| の人体発湿を除く内部発湿, kg/s

:math:`\hat{X}_{hum,i,n}` : ステップ |n| における室 |i| の人体発湿, kg/s

:math:`\hat{L}_{a,i,n}` : ステップ |n| からステップ |n+1| における潜熱負荷に関する係数, kg/(s kg/kg(DA))

:math:`\hat{L}_{b,i,n}` : ステップ |n| からステップ |n+1| における潜熱負荷に関する係数, kg/s

である。
記号の上につく :math:`\hat{ }` （ハット）は、ステップ |n| から |n+1| の期間における積算値または平均値を表す。

式(4)も同様に後退差分で離散化すると次式となる。

.. math::
    :nowrap:

    \begin{align*}
    	C_{lh,frt,i} \cdot \frac{ X_{frt,i,n+1} - X_{frt,i,n} }{ \Delta t } = G_{lh,frt,i} \cdot ( X_{r,i,n+1} - X_{frt,i,n+1} ) \tag{6}
    \end{align*}

式(6)をステップ |n+1| における室 |i| の備品等の絶対湿度 :math:`X_{frt,i,n+1}` について解くと、

.. math::
    :nowrap:

    \begin{align*}
    	X_{frt,i,n+1} = \frac{ C_{lh,frt,i} \cdot X_{frt,i,n} + \Delta t \cdot G_{lh,frt,i} \cdot X_{r,i,n+1} }{ C_{lh,frt,i} + \Delta t \cdot G_{lh,frt,i} } \tag{7}
    \end{align*}

となる。これを式(5)に代入すると、

.. math::
    :nowrap:

    \begin{align*}
        \begin{split}
            \rho_a \cdot V_{room,i} \cdot \frac{ X_{r,i,n+1} - X_{r,i,n} }{ \Delta t }
            &= \rho_a \cdot \hat{V}_{vent,out,i,n} \cdot ( X_{o,n+1} - X_{r,i,n+1} ) \\
            &+ G_{lh,frt,i} \cdot C_{lh,frt,i} \cdot \frac{ X_{frt,i,n} - X_{r,i,n+1} }{ C_{lh,frt,i} + \Delta t \cdot G_{lh,frt,i} } \\
            &+ \rho_a \cdot \sum_{j=0}^{J-1}{ \hat{V}_{vent,int,i,j,n} \cdot ( X_{r,j,n+1} - X_{r,i,n+1} ) } \\
            &+ \hat{X}_{gen,i,n} + \hat{X}_{hum,i,n} + \hat{L}_{a,i,n} \cdot X_{r,i,n+1} + \hat{L}_{b,i,n}
        \end{split}
    	\tag{8}
    \end{align*}

となる。ステップ |n+1| における室 |i| および室 |j| の絶対湿度について解くと、

.. math::
    :nowrap:

    \begin{align*}
        \begin{split}
        	& \left( \rho_a \cdot \left( \frac{ V_{room,i} }{ \Delta t } + \hat{V}_{vent,out,i,n} \right)
    	    + \frac{G_{lh,frt,i} \cdot C_{lh,frt,i} }{ C_{lh,frt,i} + \Delta t \cdot G_{lh,frt,i} } - \hat{L}_{a,i,n} \right) \cdot X_{r,i,n+1} \\
        	&- \rho_a \sum_{j=0}^{J-1}{ \hat{V}_{vent,int,i,j,n} \cdot ( X_{r,j,n+1} - X_{r,i,n+1} ) } \\
    	    &= \rho_a \cdot \frac{ V_{room,i} }{ \Delta t } \cdot X_{r,i,n} + \rho_a \cdot \hat{V}_{vent,out,i,n} \cdot X_{o,n+1} \\
        	&+ \frac{ G_{lh,frt,i} \cdot C_{lh,frt,i} }{ C_{lh,frt,i} + \Delta t \cdot G_{lh,frt,i} } \cdot X_{frt,i,n} \\
    	    &+ \hat{X}_{gen,i,n} + \hat{X}_{hum,i,n} + \hat{L}_{b,i,n}
        \end{split}
    	\tag{9}
    \end{align*}

となる。式(9)は左辺に室 |i| の絶対湿度と室 |j| の絶対湿度がでてくる連立方程式であり、行列式で表すと

.. math::
    :nowrap:

    \begin{align*}
    	( \pmb{f}_{h,wgt,n} - \pmb{ \hat{L} }_{a,n} ) \cdot \pmb{X}_{r,n+1} = \pmb{f}_{h,cst,n} + \pmb{\hat{L}}_{b,n} \tag{10}
    \end{align*}

となる。

:math:`\pmb{f}_{h,wgt,n}` は、 :math:`I \times I` の正方行列で、次式で表される。

.. math::
    :nowrap:

    \begin{align*}
    	\pmb{f}_{h,wgt,n} &= diag \left( \rho_a \left( \frac{V_{room,i} }{ \Delta t } + \hat{V}_{vent,out,i,n} \right) + \frac{ G_{lh,frt,i} \cdot C_{lh,frt,i} }{ C_{lh,frt,i} + \Delta t \cdot G_{lh,frt,i} } \right) \\
	    &- \rho_a \cdot \pmb{\hat{V}}_{vent,int,n}
    	\tag{11}
    \end{align*}

:math:`diag` は室の数を :math:`I` とすると、室 :math:`0` から :math:`I-1` の対角行列を表す。

:math:`\pmb{f}_{h,cst,n}` は :math:`I \times 1` の行列であり、その要素を :math:`F_{h,cst,i,n}` とすると、

.. math::
    :nowrap:

    \begin{align*}
    	f_{h,cst,i,n} &= \rho_a \cdot \frac{ V_{room,i} }{ \Delta t } \cdot X_{r,i,n}
	    + \rho_a \cdot \hat{V}_{vent,out,i,n} \cdot X_{o,n+1} \\
    	&+ \frac{G_{lh,frt,i} \cdot C_{lh,frt,i} }{ C_{lh,frt,i} + \Delta t \cdot G_{lh,frt,i} } \cdot X_{frt,i,n}
	    + \hat{X}_{gen,i,n} + \hat{X}_{hum,i,n}
    	\tag{12}
    \end{align*}

:math:`\pmb{\hat{L}}_{a,n}` は :math:`I \times I` の対角化行列であり、以下で定義される。

.. math::
    :nowrap:

    \begin{align*}
    	\pmb{\hat{L}}_{a,n} = diag( \hat{L}_{a,i,n} )
    \end{align*}

:math:`\pmb{\hat{L}}_{b,n}` は :math:`I \times 1` の縦行列であり、その要素は :math:`\hat{L}_{b,i,n}` である。

:math:`\pmb{\hat{V}}_{vent,int,n}` は室間換気を表す :math:`I \times I` の行列であり、例えば、室総数が3の場合で室1から室0へ60　|m3| / s の換気量がある場合は、

.. math::
    :nowrap:

    \begin{align*}
    	\pmb{\hat{V}}_{vent,int.,n}
	    = \begin{pmatrix}
      	-60 & 60 & 0 \\
  	    0   & 0  & 0 \\
  	    0   & 0  & 0
		    \end{pmatrix}
    \end{align*}

となり、室総数が3の場合で室1から室0へ 60 |m3| / s の換気量かつ室2から室0へ 30 |m3|/s の換気量がある場合は、

.. math::
    :nowrap:

    \begin{align*}
    	\pmb{\hat{V}}_{vent,int,n}
	    = \begin{pmatrix}
      	-90 & 60 & 30 \\
  	    0   & 0  &  0 \\
      	0   & 0  &  0
	    	\end{pmatrix}
    \end{align*}

となる。これを式で表すと、

.. math::
    :nowrap:

    \begin{align*}
    	\pmb{\hat{V}}_{vent,int,n}
	    &= - diag \left (
    	\sum_{j=0}^{J-1}{\hat{V}_{vent,int,0,j,n}} \  \cdots \  \sum_{j=0}^{J-1}{\hat{V}_{vent,int,i,j,n}} \  \dots \  \sum_{j=0}^{J-1}{\hat{V}_{vent,int,I-1,j,n}}
	    \right ) \\
    	&+ \begin{pmatrix}
	    0 & \cdots & \hat{V}_{vent,int,0,j,n} & \cdots & \hat{V}_{vent,int,0,J-1,n} \\
    	\vdots & \ddots & \vdots & & \vdots \\
	    \hat{V}_{vent,int,i,0,n} & \cdots & 0 & \cdots & \hat{V}_{vent,int,i,J-1,n} \\
    	\vdots & & \vdots & \ddots & \vdots \\
	    \hat{V}_{vent,int,I-1,0,n} & \cdots & \hat{V}_{vent,int,I-1,j,n} & \cdots & 0 \\
    	\end{pmatrix}
		\tag{13}
    \end{align*}

となる。

------------------------------------------------------------------------------------------------------------------------
2. 目標絶対湿度を設定する場合と設定しない場合が混在している場合の解法
------------------------------------------------------------------------------------------------------------------------

ここで、 目標とする絶対湿度を設定する場合としない場合で式(10)における未知数が異なる。
この式について、変数を指定する項目と指定しない項目とに分離すると、

.. math::
    :nowrap:

    \begin{align*}
    	( \pmb{f}_{h,wgt,n} - \pmb{\hat{L}}'_{a,n} ) \cdot ( \pmb{X}'_{r,n+1} + \pmb{X}'_{r,set,n+1} )
        = \pmb{f}_{h,cst,n} + \pmb{\hat{L}}'_{b,n} + \pmb{\hat{L}}'_{b,set,n}
    	\tag{14}
    \end{align*}

となる。ここで、室 |i| に目標とする絶対湿度を設定する場合は、定義から :math:`\pmb{\hat{L}}'_{a,n}` の |i| 成分が0になり、 :math:`\pmb{\hat{L}}'_{b,set,n}` のみが未知数となる。
ここで、 :math:`\pmb{\hat{L}}'_{b,set,n}` は絶対湿度を設定(=set)した場合の未知数としての負荷成分であることに留意されたい。未知数を左辺に既知数を右辺に整理する。

.. math::
    :nowrap:

    \begin{align*}
    	& ( \pmb{f}_{h,wgt,n} - \pmb{\hat{L}}'_{a,n} ) \cdot \pmb{X}'_{r,n+1} - \pmb{\hat{L}}'_{b,set,n} \\
	    &= - ( \pmb{f}_{h,wgt,n} - \pmb{\hat{L}}'_{a,n} ) \cdot \pmb{X}'_{r,set,n+1} + \pmb{f}_{h,cst,n} + \pmb{\hat{L}}'_{b,n}
    	\tag{15}
    \end{align*}

ここで、

.. math::
    :nowrap:

    \begin{align*}
    	\pmb{X}'_{r,n+1} = {\begin{pmatrix} X'_{r,0,n+1} & \cdots & X'_{r,i,n+1} & \cdots & X'_{r,I-1,n+1} \end{pmatrix}}^T
    \end{align*}

.. math::
    :nowrap:

    \begin{align*}
    	\pmb{\hat{L}}'_{a,n} = diag( \hat{L}'_{a,i,n} )
    \end{align*} 

.. math::
    :nowrap:

    \begin{align*}
    	\pmb{\hat{L}}'_{b,n} = {\begin{pmatrix} \hat{L}'_{b,0,n} & \cdots & \hat{L}'_{b,i,n} & \cdots & \hat{L}'_{b,I-1,n} \end{pmatrix}}^T
    \end{align*}

.. math::
    :nowrap:

    \begin{align*}
    	\pmb{X}'_{r,set,n+1} = {\begin{pmatrix} X'_{r,set,0,n+1} & \cdots & X'_{r,set,i,n+1} & \cdots & X'_{r,set,I-1,n+1} \end{pmatrix}}^T
    \end{align*}

.. math::
    :nowrap:

    \begin{align*}
    	\pmb{\hat{L}}'_{b,set,n} = {\begin{pmatrix} \hat{L}'_{b,set,0,n} & \cdots & \hat{L}'_{b,set,i,n} & \cdots & \hat{L}'_{b,set,I-1,n} \end{pmatrix}}^T
    \end{align*}

であり、

:math:`X'_{r,i,n+1}` :ステップ |n+1| における室iの絶対湿度（ただし、室 |i| の設定絶対湿度を定める場合は0とする）, kg/kg(DA)

:math:`\hat{L}'_{b,i,n}` : ステップ |n| からステップ |n+1| における室 |i| の設定潜熱負荷（加湿を正・除湿を負とする）（ただし、室 |i| の設定絶対湿度を定める場合は0とする）, kg/s

:math:`X'_{r,set,i,n+1}` : ステップ |n+1| における室 |i| の設定絶対湿度（ただし、室 |i| の設定絶対湿度を定めない場合は0とする）, kg/kg(DA)

:math:`\hat{L}'_{b,set,i,n}` : ステップ |n| からステップ |n+1| における室 |i| の潜熱負荷（加湿を正・除湿を負とする）（ただし、室 |i| の設定絶対湿度を定めない場合は0とする）, kg/s

である。ここで、 :math:`X'_{r,i,n+1}` と :math:`\hat{L}'_{b,set,i,n}` のどちらか一方は必ず0となる。
同様に、:math:`X'_{r,set,i,n+1}` と :math:`\hat{L}'_{b,i,n}` のどちらか一方は必ず0となる。

ここで、

.. math::
    :nowrap:

    \begin{align*}
        \pmb{f}'_{h,wgt,n} = \pmb{F}_{h,wgt,n} - \pmb{\hat{L}}'_{a,n}
    \end{align*}

とおくと、式(15)は、

.. math::
    :nowrap:

    \begin{align*}
    	\pmb{f}'_{h,wgt,n} \cdot \pmb{X}'_{r,n+1} - \pmb{\hat{L}}'_{b,set,n} = - \pmb{f}'_{h,wgt,n} \cdot \pmb{X}'_{r,set,n+1} + \pmb{f}_{h,cst,n} + \pmb{\hat{L}}'_{b,n} \tag{16}
    \end{align*}

となる。

:math:`X'_{r,i,n+1}` と :math:`\hat{L}'_{b,set,i,n}` のどちらか一方は必ず0となることを利用し、 :math:`\pmb{f}''_{h,wgt,n}` を :math:`I \times J` の行列とし、
その要素を次式で表される :math:`f''_{h,wgt,i,j,n}` とすると、

.. math::
    :nowrap:

    \begin{align*}
    	f''_{h,wgt,i,j,n} = \begin{cases}
            f'_{h,wgt,i,j,n} & ( \hat{f}_{set,j,n} = 0 ) \\
            - \delta_{i,j} & ( \hat{f}_{set,j,n} = 1 )
        \end{cases}
    	\tag{17}
    \end{align*}

とおくと、

.. math::
    :nowrap:

    \begin{align*}
    	& \pmb{f}''_{h,wgt,n} \cdot ( \pmb{X}'_{r,n+1} + \pmb{\hat{L}}'_{b,set,n} ) \\
	    &= - \pmb{f}'_{h,wgt,n} \cdot \pmb{X}'_{r,set,n+1} + \pmb{f}_{h,cst,n} + \pmb{\hat{L}}'_{b,n}
    	\tag{18}
    \end{align*}

となり、

.. math::
    :nowrap:

    \begin{align*}
    	\pmb{k}_n
        &= \pmb{X}'_{r,n+1} + \pmb{\hat{L}}'_{b,set,n} \\
        &= {\pmb{f}''}_{h,wgt,n}^{-1} \cdot ( - \pmb{f}'_{h,wgt,n} \cdot \pmb{X}'_{r,set,n+1} + \pmb{f}_{h,cst,n} + \pmb{\hat{L}}'_{b,n} )
    	\tag{19}
    \end{align*}

を解けばよい。ここで、:math:`\hat{f}_{set,j,n}` は、室 |j| において、
絶対湿度を指定する場合（加湿・除湿量は指定された室の絶対湿度を満たすように成り行きで定まる場合）を1、
室の絶対湿度を指定せず成り行きの絶対湿度とする場合（加湿・除湿を行わない又は加湿・除湿を室の絶対湿度に依らず定められた量行う場合）を0とする。

また、

.. math::
    :nowrap:

    \begin{align*}
    	\pmb{k}_n = \pmb{X}'_{r,n+1} + \pmb{\hat{L}}'_{b,set,n}
    \end{align*}

における、室 |i| の要素 :math:`X'_{r,i,n+1}` または :math:`\hat{L}'_{b,set,i,n}` について、どちらかは必ずゼロになるため、前述の :math:`\hat{f}_{set,i,n}` （添字は |i| とした）を用いて、

.. math::
    :nowrap:

    \begin{align*}
    	X_{r,i,n+1} = \begin{cases}
	    	k_{i,n} & ( \hat{f}_{set,i,n} = 0 ) \\
		    X'_{r,set,i,n+1} & ( \hat{f}_{set,i,n} = 1 )
    	\end{cases}
    	\tag{20-1}
    \end{align*}

.. math::
    :nowrap:

    \begin{align*}
    	\hat{L}_{b,i,n} = \begin{cases}
	    	\hat{L}'_{b,i,n} & ( \hat{f}_{set,i,n} = 0 ) \\
		    k_{i,n} & ( \hat{f}_{set,i,n} = 1 )
    	\end{cases}
    	\tag{20-2}
    \end{align*}

と表すことができる。

この際、潜熱負荷は、

.. math::
    :nowrap:

    \begin{align*}
        \pmb{\hat{L}}_{L,n} = \pmb{\hat{L}}_{a,n} \cdot \pmb{X}_{r,n+1} + \pmb{\hat{L}}_{b,n} \tag{21}
    \end{align*}

で表される。

------------------------------------------------------------------------------------------------------------------------
3） 加湿・除湿に係る係数の定め方
------------------------------------------------------------------------------------------------------------------------

係数 :math:`\pmb{\hat{L}}_{a,n}` ・ :math:`\pmb{\hat{L}}_{b,n}` の決定方法を記す。

これらの係数は、すべての要素が0である行列として、以下の場合に基づいて各要素に値を加算していく。

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ア） 除湿・加湿を行わない場合
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

係数 :math:`\pmb{\hat{L}}_{a,n}` ・ :math:`\pmb{\hat{L}}_{b,n}` に対する加算は行わない。


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
イ） 一定量の除湿・加湿を行う場合
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

係数 :math:`\pmb{\hat{L}}_{a,n}` に対する加算は行わない。

係数 :math:`\pmb{\hat{L}}_{b,n}` の要素 :math:`\hat{L}_{b,i,n}` に対して、　:math:`\hat{L}_{L,const,i,n}` を加算する。
ここで、

:math:`\hat{L}_{L,const,i,n}`
    | ステップ |n| からステップ |n+1| における室 |i| の潜熱負荷（加湿を正・除湿を負とする）, kg/s

である。

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ウ）室の絶対湿度に応じて一定量の除湿を行う場合
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

室の絶対湿度に応じて加湿量が決まる機構をもつ設備は存在しないため、本パターンにおいては、除湿のみを考える。

係数 :math:`\hat{L}_{a,n}` ・ :math:`\hat{L}_{b,n}` の決め方は設備固有のものである。

多くの場合、この方法は除湿を行う場合に採用される。
熱交換器表面の飽和絶対湿度よりも室の絶対湿度が上回っている場合は除湿を行うが、下回っている場合は除湿が行われない。
この場合、まず空調していない場合の絶対湿度を計算し、機器の熱交換器表面の飽和絶対湿度をそれが下回っている場合に除湿が行われるとし、
上回っている場合は「ア） 除湿・加湿を行わない場合」と同じ考え方で特に加算は行わない。
なお、本評価は室間換気を考慮した全室の連成計算のため、厳密に言えば他の部屋で加湿を行っている場合は、対象とする室がその影響を受けて除湿が行われるということがありうる。
しかし、これを考慮すると、収束計算等が必要となるため、本評価ではこれを考慮しない。
（その結果、厳密には、室の絶対湿度が熱交換器表面の飽和絶対湿度より大きい場合であっても、潜熱負荷が生じないということがありうる。）

次に、係数 :math:`\hat{L}_{a,n}` ・ :math:`\hat{L}_{b,n}` の決め方を対流型の空調と放射型の空調の場合に分けて記す。

i) 対流型の空調の場合

機器の吹き出し絶対湿度 :math:`X_{eq,out}` は吸い込み湿度 :math:`X_{eq,in}` と熱交換器表面の飽和絶対湿度 :math:`X_{eq,srf,ex}` を用いて次のように表される。

.. math::
    :nowrap:

    \begin{align*}
    	X_{eq,out} = BF \cdot X_{eq,in} + ( 1 - BF ) \cdot X_{eq,srf,ex} \tag{b22}
    \end{align*}

ここで、

:math:`X_{eq,out}`
    | 機器の室内機の吹き出し絶対湿度, kg / kg(DA)
:math:`X_{eq,in}`
    | 機器の室内機の吸い込み絶対湿度, kg / kg(DA)
:math:`X_{eq,srf,ex}`
    | 機器の室内機の熱交換器表面の絶対湿度, kg / kg(DA)
:math:`BF`
    | 機器のバイパスファクター

である。機器の室内機の吹き出し風量を :math:`V_{eq}` とすると、除湿量は、

.. math::
    :nowrap:

    \begin{align*}
    	L_{L} = - V_{eq} \cdot \rho_a \cdot ( X_{eq,in} - X_{eq,out} ) \tag{b23}
    \end{align*}

と表される。ここで、

:math:`L_L`
    | 機器の除湿量, kg / s
:math:`V_{eq}`
    | 機器の室内機の吹き出し風量, |m3| / s

である。

機器の室内機の吸い込み絶対湿度 :math:`X_{eq,in}` は室の絶対湿度 :math:`X_r` に等しいとし、式(b23)に式(b22)を代入すると、

.. math::
    :nowrap:

    \begin{align*}
    	L_L &= - V_{eq} \cdot \rho_a \cdot ( X_{eq,in} - X_{eq,out} ) \\
            &= - V_{eq} \cdot \rho_a \cdot ( X_{eq,in} - (BF \cdot X_{eq,in} + ( 1 - BF ) \cdot X_{eq,srf,ex} )) \\
            &= - V_{eq} \cdot \rho_a \cdot ( 1 - BF ) \cdot ( X_r - X_{eq,srf,ex} )
    	\tag{b24}
    \end{align*}

ここで、潜熱負荷 :math:`L_L` を

.. math::
    :nowrap:

    \begin{align*}
    	L_L = L_a \cdot X_r + L_b
    \end{align*}

と表したとすると、

.. math::
    :nowrap:

    \begin{align*}
    	L_a = - V_{eq} \cdot \rho_a \cdot ( 1 - BF ) \tag{b25}
    \end{align*}

.. math::
    :nowrap:

    \begin{align*}
    	L_b = V_{eq} \cdot \rho_a \cdot ( 1 - BF ) \cdot X_{RAC,eq,ex} \tag{b26}
    \end{align*}

となる。

次に、ルームエアコンディショナーのように各室に対応して設置し、吸い込みと吹き出しが同じ室で行われる個別空調の場合と、
ダクト式セントラル空調のように吸い込みと吹き出しが別の室（例えば非居室から吸い込み、各居室に吹き出す）で行われる居室間空調の場合とで分けて考える。

i-1) 個別空調の場合（ルームエアコンディショナー）

室 |i| に設置するルームエアコンディショナー等の個別空調（以下、単に機器という）の
