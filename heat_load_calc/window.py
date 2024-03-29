from enum import Enum, auto
from typing import Optional, Tuple
from math import sin, cos, pi

class Window:
    """窓を表すクラス
    """

    class FlameType(Enum):
        """フレーム材質
        """

        # 樹脂製製建具
        RESIN = auto()
        # 木製建具
        WOOD = auto()
        # 木と金属の複合材料製建具
        MIXED_WOOD = auto()
        # 樹脂と金属の複合材料製建具
        MIXED_RESIN = auto()
        # 金属製建具
        ALUMINUM = auto()
    
    class GlassType(Enum):
        """ガラスの構成
        """

        # 単層
        SINGLE = 'single'
        # 複層
        MULTIPLE = 'multiple'


    def __init__(self, u_w_j: float, eta_w_j: float, glass_type: GlassType, r_a_w_g_j: Optional[float] = None, flame_type: FlameType = FlameType.MIXED_WOOD):
        """

        Args:
            u_w_j: 境界 j の窓の熱損失係数, W/m2K
            eta_w_j: 境界 j の窓の日射熱取得率, -
            glass_type: 境界 j の窓のガラス構成
            r_a_w_g_j: 境界 j の窓の面積に対するグレージングの面積の比, -
            flame_type: _description_. Defaults to FlameType.MIXED.
        """

        self._glass_type = glass_type

        self._u_w_f_j = self._get_u_w_f_j(flame_type=flame_type)
        self._r_a_w_g_j = self._get_r_a_w_g_j(r_a_w_g_j=r_a_w_g_j, flame_type=flame_type)
        self._u_w_g_j = self._get_u_w_g_j(u_w_j=u_w_j, u_w_f_j=self._u_w_f_j, r_a_w_g_j=self._r_a_w_g_j)
        self._eta_w_g_j = self._get_eta_w_g_j(eta_w_j=eta_w_j, r_a_w_g_j=self._r_a_w_g_j)
        r_w_o_w, r_w_i_w, r_w_o_s, r_w_i_s = self._get_r_w()
        self._u_w_g_s_j = self._get_u_w_g_s_j(u_w_g_j=self._u_w_g_j, r_w_o_w=r_w_o_w, r_w_i_w=r_w_i_w, r_w_o_s=r_w_o_s, r_w_i_s=r_w_i_s)
        self._r_r_w_g_j = self._get_r_r_w_g_j(u_w_g_j=self._u_w_g_j, u_w_g_s_j=self._u_w_g_s_j, r_w_o_w=r_w_o_w, r_w_i_w=r_w_i_w, r_w_o_s=r_w_o_s, glass_type=glass_type)
        self._rho_w_g_s1f_j = self._get_rho_w_g_s1f_j(r_r_w_g_j=self._r_r_w_g_j, eta_w_g_j=self._eta_w_g_j)
        self._rho_w_g_s2f_j = self._get_rho_w_g_s2f_j(glass_type=glass_type)
        self._tau_w_g_j = self._get_tau_w_g_j(eta_w_g_j=self._eta_w_g_j, r_r_w_g_j=self._r_r_w_g_j, rho_w_g_s1f_j=self._rho_w_g_s1f_j, rho_w_g_s2f_j=self._rho_w_g_s2f_j, glass_type=glass_type)
        self._tau_w_g_s1_j = self._get_tau_w_g_s1_j(tau_w_g_j=self._tau_w_g_j, rho_w_g_s2f_j=self._rho_w_g_s2f_j, glass_type=glass_type)
        self._tau_w_g_s2_j = self._get_tau_w_g_s2_j(tau_w_g_s1_j=self._tau_w_g_s1_j, glass_type=glass_type)
        self._rho_w_g_s1b_j = self._get_rho_w_g_s1b_j(tau_w_g_s1_j=self._tau_w_g_s1_j, glass_type=glass_type)
        self._tau_w_r_j, self._tau_w_s_j, self._eta_w_r_j, self._eta_w_s_j, self._alpha_w_r_j, self._alpha_w_s_j = self._get_tau_eta_alpha_w_j()

    @property
    def u_w_f_j(self):
        """建具部分の熱損失係数（U値）を取得する。

        Returns:
            境界 j の窓の建具部分の熱損失係数（U値）, W/m2K
        """
        return self._u_w_f_j

    @property
    def r_a_w_g_j(self):
        """窓の面積に対するグレージングの面積の比を取得する。

        Returns:
            境界 j の窓の面積に対するグレージングの面積の比, -
        """
        return self._r_a_w_g_j

    @property
    def u_w_g_j(self):
        """窓のガラス部分の熱損失係数（U値）を取得する。

        Returns:
            境界 j の窓のガラス部分の熱損失係数（U値）, W/m2K
        """
        return self._u_w_g_j
    
    @property
    def eta_w_g_j(self):
        """窓のガラス部分の日射熱取得率を取得する。

        Returns:
            境界 j の窓のガラス部分の日射熱取得率, -
        """
        return self._eta_w_g_j

    @property
    def tau_w_g_j(self):
        """窓のガラス部分の日射透過率を取得する。

        Returns:
            境界 j の窓のガラス部分の日射透過率, -
        """
        return self._tau_w_g_j

    @property
    def tau_w_r_j(self):
        """窓の地面反射に対する日射透過率を取得する。
        Returns:
            境界 j の窓の地面反射に対する日射透過率, -
        """
        return self._tau_w_r_j

    @property
    def tau_w_s_j(self):
        """窓の天空放射に対する日射透過率を取得する。
        Returns:
            境界 j の窓の天空放射に対する日射透過率, -
        """
        return self._tau_w_s_j

    @property
    def alpha_w_r_j(self):
        """窓の地面反射に対する日射吸収率を取得する。
        Returns:
            境界 j の窓の地面反射に対する日射吸収率, -
        """
        return self._alpha_w_r_j

    @property
    def alpha_w_s_j(self):
        """窓の天空放射に対する日射吸収率を取得する。
        Returns:
            境界 j の窓の天空放射に対する日射吸収率, -
        """
        return self._alpha_w_s_j

    @property
    def eta_w_r_j(self):
        """窓の地面反射に対する日射熱取得率を取得する。
        Returns:
            境界 j の窓の地面反射に対する日射熱取得率, -
        """
        return self._eta_w_r_j

    @property
    def eta_w_s_j(self):
        """窓の天空放射に対する日射熱取得率を取得する。
        Returns:
            境界 j の窓の天空放射に対する日射熱取得率, -
        """
        return self._eta_w_s_j

    @staticmethod
    def _get_u_w_f_j(flame_type: FlameType) -> float:
        """建具部分の熱損失係数（U値）を取得する。

        Args:
            flame_type: 建具（フレーム）材質の種類

        Returns:
            境界 j の窓の建具部分の熱損失係数（U値）, W/m2K
        """

        return  {
            Window.FlameType.RESIN: 2.2,
            Window.FlameType.WOOD: 2.2,
            Window.FlameType.ALUMINUM: 6.6,
            Window.FlameType.MIXED_WOOD: 4.7,
            Window.FlameType.MIXED_RESIN: 4.7
        }[flame_type]
    
    @staticmethod
    def _get_r_a_w_g_j(r_a_w_g_j: Optional[float], flame_type: FlameType) -> float:
        """窓の面積に対するグレージングの面積の比が指定されていない場合に枠（フレーム）材質の種類に応じてデフォルト値を定める。

        Args:
            r_a_w_g_j: 境界 j の窓の面積に対するグレージングの面積の比, -
            flame_type: 建具（フレーム）材質の種類
        Returns:
            境界 j の窓の面積に対するグレージングの面積の比, -
        """

        if r_a_w_g_j is None:
            return {
                Window.FlameType.RESIN: 0.72,
                Window.FlameType.WOOD: 0.72,
                Window.FlameType.ALUMINUM: 0.8,
                Window.FlameType.MIXED_WOOD: 0.8,
                Window.FlameType.MIXED_RESIN: 0.8
            }[flame_type]
        else:
            return r_a_w_g_j

    @staticmethod
    def _get_u_w_g_j(u_w_j: float, u_w_f_j: float, r_a_w_g_j: float) -> float:
        """窓のガラス部分の熱損失係数（U値）を取得する。

        Args:
            u_w_j: 境界 j の窓の熱損失係数, W/m2K
            u_w_f_j: 境界 j の窓の建具部分の熱損失係数（U値）, W/m2K
            r_a_w_g_j: 境界 j の窓の面積に対するグレージングの面積の比, -

        Returns:
            境界 j の窓のガラス部分の熱損失係数（U値）, W/m2K
        """
        return (u_w_j - u_w_f_j * (1 - r_a_w_g_j)) / r_a_w_g_j
        
    @staticmethod
    def _get_eta_w_g_j(eta_w_j: float, r_a_w_g_j: float) -> float:
        """_summary_

        Args:
            eta_w_j: 境界 j の窓の日射熱取得率
            r_a_w_g_j: 境界 j の窓の面積に対するグレージングの面積の比, -

        Returns:
            境界 j の窓のガラス部分の日射熱取得率, -
        """
        return eta_w_j / r_a_w_g_j

    @staticmethod
    def _get_r_w() -> Tuple[float, float, float, float]:
        """窓の表面熱伝達抵抗を求める。

        Returns:
            窓の室外側表面熱伝達抵抗（冬季条件）, m2K/W
            窓の室内側表面熱伝達抵抗（冬季条件）, m2K/W
            窓の室外側表面熱伝達抵抗（夏季条件）, m2K/W
            窓の室内側表面熱伝達抵抗（夏季条件）, m2K/W
        """
        r_w_o_w = 0.0415
        r_w_i_w = 0.1228
        r_w_o_s = 0.0756
        r_w_i_s = 0.1317
        return r_w_o_w, r_w_i_w, r_w_o_s, r_w_i_s

    @staticmethod
    def _get_u_w_g_s_j(u_w_g_j: float, r_w_o_w: float, r_w_i_w: float, r_w_o_s: float, r_w_i_s: float) -> float:
        """窓のガラス部分の熱損失係数（夏期条件）を計算する。

        Args:
            u_w_g_j: 境界jの窓のガラス部分の熱損失係数（U値）, W/m2K
            r_w_o_w: 窓の室外側表面熱伝達抵抗（冬期条件）, m2K/W
            r_w_i_w: 窓の室内側表面熱伝達抵抗（冬期条件）, m2K/W
            r_w_o_s: 窓の室外側表面熱伝達抵抗（夏期条件）, m2K/W
            r_w_i_s: 窓の室内側表面熱伝達抵抗（夏期条件）, m2K/W

        Returns:
            境界jの窓のガラス部分の熱損失係数（夏期条件）, W/m2K
        """
        return 1 / (1 / u_w_g_j - r_w_o_w - r_w_i_w + r_w_o_s + r_w_i_s)

    @staticmethod
    def _get_r_r_w_g_j(u_w_g_j: float, u_w_g_s_j: float, r_w_o_w: float, r_w_i_w: float, r_w_o_s: float, glass_type: GlassType) -> float:
        """窓のガラス部分の日射吸収量に対する室内側に放出される量の割合を計算する。

        Args:
            u_w_g_j: 境界jの窓のガラス部分の熱損失係数（U値）, W/m2K
            u_w_g_s_j: 境界jの窓のガラス部分の熱損失係数（夏期条件）, W/m2K
            r_w_o_w: 窓の室外側表面熱伝達抵抗（冬期条件）, m2K/W
            r_w_i_w: 窓の室内側表面熱伝達抵抗（冬期条件）, m2K/W
            r_w_o_s: 窓の室外側表面熱伝達抵抗（夏期条件）, m2K/W
            glass_type: 境界 j の窓のガラス構成

        Returns:
            境界jの窓のガラス部分の日射吸収量に対する室内側に放出される量の割合, -
        """

        if glass_type == Window.GlassType.SINGLE:
            return (1 / 2 * (1 / u_w_g_j - r_w_o_w - r_w_i_w) + r_w_o_s) * u_w_g_s_j
        elif glass_type == Window.GlassType.MULTIPLE:
            # 複層ガラスにおける窓の中空層の熱伝達抵抗, m2K/W
            r_w_air = 0.003
            return (1 / 4 * (1 / u_w_g_j - r_w_o_w - r_w_i_w - r_w_air) + r_w_o_s) * u_w_g_s_j
        else:
            raise ValueError()

    @staticmethod
    def _get_rho_w_g_s1f_j(r_r_w_g_j: float, eta_w_g_j: float) -> float:
        """窓のガラス部分の室外側から1枚目の板ガラスの反射率（正面側）を計算する。

        Args:
            r_r_w_g_j: 境界jの窓のガラス部分の日射吸収量に対する室内側に放出される量の割合, -
            eta_w_g_j: 境界jの窓のガラス部分の日射熱取得率, -
        Returns:
            境界jの窓のガラス部分の室外側から1枚目の板ガラスの反射率（正面側）, -
        """
        t_j = (-1.846 * r_r_w_g_j + ((1.846 * r_r_w_g_j)**2 + 4 * (1 - 1.846 * r_r_w_g_j) * eta_w_g_j)**0.5) / (2 * (1 - 1.846 * r_r_w_g_j))
        return 0.923 * (t_j ** 2) - 1.846 * t_j + 1

    @staticmethod
    def _get_rho_w_g_s2f_j(glass_type: GlassType) -> Optional[float]:
        """窓のガラス部分の室外側から2枚目の板ガラスの反射率（正面側）を計算する。

        Args:
            glass_type: 境界 j の窓のガラス構成

        Returns:
            境界 j の窓のガラス部分の室外側から2枚目の板ガラスの反射率（正面側）

        Notes:
            複層ガラスの場合のみ定義される。
        """
        if glass_type == Window.GlassType.SINGLE:
            return None
        elif glass_type == Window.GlassType.MULTIPLE:
            return 0.077
        else:
            raise ValueError()

    @staticmethod
    def _get_tau_w_g_j(eta_w_g_j: float, r_r_w_g_j: float, rho_w_g_s1f_j: float, rho_w_g_s2f_j: Optional[float], glass_type: GlassType) -> float:
        """窓のガラス部分の日射透過率を計算する。

        Args:
            eta_w_g_j: 境界 j の窓のガラス部分の日射熱取得率, -
            r_r_w_g_j: 境界 j の窓のガラス部分の日射吸収量に対する室内側に放出される量の割合, -
            rho_w_g_s1f_j: 境界 j の窓のガラス部分の室外側から1枚目の板ガラスの反射率（正面側）, -
            rho_w_g_s2f_j: 境界 j の窓のガラス部分の室外側から2枚目の板ガラスの反射率（正面側）, -
            glass_type: 境界 j の窓のガラス構成

        Returns:
            境界 j の窓のガラス部分の日射透過率, -
        """

        if glass_type == Window.GlassType.SINGLE:
            return (eta_w_g_j - (1 - rho_w_g_s1f_j) * r_r_w_g_j) / (1 - r_r_w_g_j)
        elif glass_type == Window.GlassType.MULTIPLE:
            return (eta_w_g_j - (1 - rho_w_g_s1f_j) * r_r_w_g_j) / ((1 - r_r_w_g_j) - rho_w_g_s2f_j * r_r_w_g_j)
        else:
            raise ValueError()
    
    @staticmethod
    def _get_tau_w_g_s1_j(tau_w_g_j: float, rho_w_g_s2f_j: Optional[float], glass_type: GlassType) -> float:
        """窓のガラス部分の室外側から1枚目の板ガラスの透過率を計算する。

        Args:
            tau_w_g_j: 境界 j の窓のガラス部分の日射透過率, -
            rho_w_g_s2f_j: 境界 j の窓のガラス部分の室外側から2枚目の板ガラスの反射率（正面側）, -
            glass_type: 境界 j の窓のガラス構成

        Returns:
            境界 j の窓のガラス部分の室外側から1枚目の板ガラスの透過率, -
        """
        
        if glass_type == Window.GlassType.SINGLE:
            return tau_w_g_j
        elif glass_type == Window.GlassType.MULTIPLE:
            return (0.379 * rho_w_g_s2f_j * tau_w_g_j + ((0.379 * rho_w_g_s2f_j * tau_w_g_j)**2 - 4 * (0.379 * rho_w_g_s2f_j - 1) * tau_w_g_j )**0.5) / 2
        else:
            raise ValueError()

    @staticmethod
    def _get_tau_w_g_s2_j(tau_w_g_s1_j: Optional[float], glass_type: GlassType) -> Optional[float]:
        """窓のガラス部分の室外側から2枚目の板ガラスの透過率を計算する。

        Args:
            tau_w_g_s1_j: 境界jの窓のガラス部分の室外側から1枚目の板ガラスの透過率, -
            glass_type: 境界 j の窓のガラス構成
        Returns:
            境界jの窓のガラス部分の室外側から2枚目の板ガラスの透過率, -
        Notes:
            複層ガラスの場合のみ定義される。
        """
        if glass_type == Window.GlassType.SINGLE:
            return None
        elif glass_type == Window.GlassType.MULTIPLE:
            return tau_w_g_s1_j
        else:
            raise ValueError()

    @staticmethod
    def _get_rho_w_g_s1b_j(tau_w_g_s1_j: Optional[float], glass_type: GlassType) -> Optional[float]:
        """窓のガラス部分の室外側から1枚目の板ガラスの反射率（背面側）を計算する。

        Args:
            tau_w_g_s1_j: 境界 j の窓のガラス部分の室外側から1枚目の板ガラスの透過率, -
            glass_type: 境界 j の窓のガラス構成
        Returns:
            境界 j の窓のガラス部分の室外側から1枚目の板ガラスの反射率（背面側）, -
        Notes:
            複層ガラスの場合のみ定義される。
        """
        if glass_type == Window.GlassType.SINGLE:
            return None
        elif glass_type == Window.GlassType.MULTIPLE:
            return 0.379 * (1 - tau_w_g_s1_j)
        else:
            raise ValueError()

    @staticmethod
    def _get_rho_n_phi(phi: float) -> float:
        """規準化反射率を計算する。

        Args:
            phi: 入射角, rad
        Returns:
            規準化反射率, -
        """
        ms_rho = [1.000, -5.189, 12.392, -16.593, 11.851, -3.461]
        return sum([m_rho * (cos(phi) ** k) for (k, m_rho) in enumerate(ms_rho)])
        
    @staticmethod
    def _get_tau_n_phi(phi: float) -> float:
        """規準化透過率を計算する。

        Args:
            phi: 入射角, rad

        Returns:
            規準化透過率
        """
        ms_tau = [0.000, 2.552, 1.364, -11.388, 13.617, -5.146]
        return sum([m_tau * (cos(phi) ** k) for (k, m_tau) in enumerate(ms_tau)])

    def _get_rho_w_g_s2f_j_phi(self, phi: float) -> float:
        """任意の入射角に対する境界 j の窓のガラス部分の室外側から2枚目の板ガラスの反射率（正面側）を計算する。
        Args:
            phi: 入射角, rad
        Returns:
            境界 j の窓のガラス部分の室外側から2枚目の板ガラスの反射率（正面側）, -
        Notes:
            この値は複層ガラスのみ計算される。
        """
        return self._rho_w_g_s2f_j + (1 - self._rho_w_g_s2f_j) * self._get_rho_n_phi(phi=phi)

    def _get_rho_w_g_s1b_j_phi(self, phi: float) -> float:
        """任意の入射角に対する境界 j の窓のガラス部分の室外側から1枚目の板ガラスの反射率（背面側）を計算する。
        Args:
            phi: 入射角, rad
        Returns:
            境界 j の窓のガラス部分の室外側から1枚目の板ガラスの反射率（背面側）, -
        Notes:
            この値は複層ガラスのみ計算される。
        """
        return self._rho_w_g_s1b_j + (1 - self._rho_w_g_s1b_j) * self._get_rho_n_phi(phi=phi)

    def _get_rho_w_g_s1f_j_phi(self, phi: float) -> float:
        """任意の入射角に対する境界 j の窓のガラス部分の室外側から1枚目の板ガラスの反射率（正面側）を計算する。
        Args:
            phi: 入射角, rad
        Returns:
            境界 j の窓のガラス部分の室外側から1枚目の板ガラスの反射率（正面側）, -
        """
        return self._rho_w_g_s1f_j + (1 - self._rho_w_g_s1f_j) * self._get_rho_n_phi(phi=phi)

    def _get_tau_w_g_s2_j_phi(self, phi: float) -> float:
        """任意の入射角に対する境界 j の窓のガラス部分の室外側から2枚目の板ガラスの透過率を計算する。
        Args:
            phi: 入射角, rad
        Returns:
            境界 j の窓のガラス部分の室外側から2枚目の板ガラスの透過率, -
        Notes:
            この値は複層ガラスのみ計算される。
        """
        return self._tau_w_g_s2_j * self._get_tau_n_phi(phi=phi)

    def _get_tau_w_g_s1_j_phi(self, phi: float) -> float:
        """任意の入射角に対する境界 j の窓のガラス部分の室外側から1枚目の板ガラスの透過率を計算する。
        Args:
            phi: 入射角, rad
        Returns:
            境界 j の窓のガラス部分の室外側から1枚目の板ガラスの透過率, -
        """
        return self._tau_w_g_s1_j * self._get_tau_n_phi(phi=phi)

    def _get_rho_w_g_j_phi(self, phi: float) -> float:
        """任意の入射角に対する境界 j の窓のガラス部分の日射反射率を計算する。
        Args:
            phi: 入射角, rad
        Returns:
            境界 j の窓のガラス部分の日射反射率, -
        """

        if self._glass_type == Window.GlassType.SINGLE:
            rho_w_g_s1f_j_phi = self._get_rho_w_g_s1f_j_phi(phi=phi)
            return rho_w_g_s1f_j_phi
        elif self._glass_type == Window.GlassType.MULTIPLE:
            rho_w_g_s1f_j_phi = self._get_rho_w_g_s1f_j_phi(phi=phi)
            rho_w_g_s1b_j_phi = self._get_rho_w_g_s1b_j_phi(phi=phi)
            rho_w_g_s2f_j_phi = self._get_rho_w_g_s2f_j_phi(phi=phi)
            tau_w_g_s1_j_phi = self._get_tau_w_g_s1_j_phi(phi=phi)
            tau_w_g_s2_j_phi = self._get_tau_w_g_s2_j_phi(phi=phi)
            return rho_w_g_s1f_j_phi + tau_w_g_s1_j_phi * tau_w_g_s2_j_phi * rho_w_g_s2f_j_phi / (1 - min(rho_w_g_s1b_j_phi * rho_w_g_s2f_j_phi, 0.9999))
        else:
            raise ValueError()
    
    def _get_tau_w_g_j_phi(self, phi: float) -> float:
        """任意の入射角に対する境界 j の窓のガラス部分の日射透過率を計算する。
        Args:
            phi: 入射角, rad
        Returns:
            境界 j の窓のガラス部分の日射透過率, -
        """

        if self._glass_type == Window.GlassType.SINGLE:
            tau_w_g_s1_j_phi = self._get_tau_w_g_s1_j_phi(phi=phi)
            return tau_w_g_s1_j_phi
        elif self._glass_type == Window.GlassType.MULTIPLE:
            rho_w_g_s1b_j_phi = self._get_rho_w_g_s1b_j_phi(phi=phi)
            rho_w_g_s2f_j_phi = self._get_rho_w_g_s2f_j_phi(phi=phi)
            tau_w_g_s1_j_phi = self._get_tau_w_g_s1_j_phi(phi=phi)
            tau_w_g_s2_j_phi = self._get_tau_w_g_s2_j_phi(phi=phi)
            return tau_w_g_s1_j_phi * tau_w_g_s2_j_phi / (1 - min(rho_w_g_s1b_j_phi * rho_w_g_s2f_j_phi, 0.9999))
        else:
            raise ValueError()

    def _get_alpha_w_g_j_phi(self, phi: float) -> float:
        """任意の入射角に対する境界 j の窓のガラス部分の日射吸収率を取得する。
        Args:
            phi: 入射角, rad
        Returns:
            float: 境界 j の窓のガラス部分の日射吸収率, -
        """
        tau_w_g_j_phi = self._get_tau_w_g_j_phi(phi=phi)
        rho_w_g_j_phi = self._get_rho_w_g_j_phi(phi=phi)
        return 1 - tau_w_g_j_phi - rho_w_g_j_phi

    def _get_eta_w_g_j_phi(self, phi: float) -> float:
        """任意の入射角に対する境界 j の窓のガラス部分の日射熱取得率を取得する。
        Args:
            phi: 入射角, rad
        Returns:
            境界 j の窓のガラス部分の日射熱取得率, -
        """

        tau_w_g_j_phi = self._get_tau_w_g_j_phi(phi=phi)
        rho_w_g_j_phi = self._get_rho_w_g_j_phi(phi=phi)
        return tau_w_g_j_phi + (1 - tau_w_g_j_phi - rho_w_g_j_phi) * self._r_r_w_g_j

    def _get_tau_w_j_phi(self, phi: float) -> float:
        """任意の入射角に対する境界 j の窓の日射透過率を取得する。
        Args:
            phi: 入射角, rad
        Returns:
            境界 j の窓の日射透過率, -
        """
        return self._get_tau_w_g_j_phi(phi=phi) * self.r_a_w_g_j
    
    def _get_alpha_w_j_phi(self, phi: float) -> float:
        """任意の入射角に対する境界 j の窓の日射吸収率を取得する。
        Args:
            phi: 入射角, rad
        Returns:
            境界 j の窓の日射吸収率, -
        """
        return self._get_alpha_w_g_j_phi(phi=phi) * self.r_a_w_g_j

    def _get_eta_w_j_phi(self, phi: float)-> float:
        """任意の入射角に対する境界 j の窓の日射熱取得率を取得する。
        Args:
            phi: 入射角, rad
        Returns:
            境界 j の窓の日射熱取得率, -
        """
        return self._get_eta_w_g_j_phi(phi=phi) * self._r_a_w_g_j

    def _get_tau_eta_alpha_w_j(self) -> Tuple[float, float, float, float, float, float]:
        """境界 j の窓の天空放射または地面反射に対する日射熱取得率または日射透過率を計算する。
        Returns:
            境界 j の窓の地面反射に対する日射透過率, -
            境界 j の窓の天空放射に対する日射透過率, -
            境界 j の窓の地面反射に対する日射熱取得率, -
            境界 j の窓の天空放射に対する日射熱取得率, -
            境界 j の窓の地面反射に対する日射吸収率, -
            境界 j の窓の天空放射に対する日射吸収率, -
        """
        M = 1000
        ms = list(range(1, M + 1))
        phis_m = [pi / 2 * (m - 1 / 2) / M for m in ms]
        tau_w_c_j = pi / M * sum([self._get_tau_w_j_phi(phi=phi_m) * sin(phi_m) * cos(phi_m) for phi_m in phis_m])
        eta_w_c_j = pi / M * sum([self._get_eta_w_j_phi(phi=phi_m) * sin(phi_m) * cos(phi_m) for phi_m in phis_m])
        alpha_w_c_j = pi / M * sum([self._get_alpha_w_j_phi(phi=phi_m) * sin(phi_m) * cos(phi_m) for phi_m in phis_m])
        tau_w_r_j = tau_w_c_j
        tau_w_s_j = tau_w_c_j
        eta_w_r_j = eta_w_c_j
        eta_w_s_j = eta_w_c_j
        alpha_w_r_j = alpha_w_c_j
        alpha_w_s_j = alpha_w_c_j

        return tau_w_r_j, tau_w_s_j, eta_w_r_j, eta_w_s_j, alpha_w_r_j, alpha_w_s_j

    def get_tau_w_j_n(self, phi_n: float) -> float:
        """窓の日射透過率を計算する。
        Args:
            phi_n: ステップ n における直達日射の入射角, rad
        Returns:
            ステップ n における境界 j の窓の日射透過率
        """
        return self._get_tau_w_j_phi(phi=phi_n)

    def get_alpha_w_j_n(self, phi_n: float) -> float:
        """窓の日射吸収率を計算する。
        Args:
            phi_n: ステップ n における直達日射の入射角, rad
        Returns:
            ステップ n における境界 j の窓の日射吸収率
        """
        return self._get_alpha_w_j_phi(phi=phi_n)

    def get_eta_w_j_n(self, phi_n: float) -> float:
        """窓の日射透過率を計算する。
        Args:
            phi_n: ステップ n における直達日射の入射角, rad
        Returns:
            ステップ n における境界 j の窓の日射透過率
        """
        return self._get_eta_w_j_phi(phi=phi_n)
    

