"""
États Polyvagaux - Les trois états neuro-numériques fondamentaux
================================================================

Implémentation de la tripartition polyvagale pour les systèmes numériques :
- VENTRAL : État de sécurité, connexion et engagement social
- SYMPATHETIC : État de mobilisation, activation et réactivité
- DORSAL : État d'effondrement, conservation et protection
"""

from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, Any, Optional, List
from datetime import datetime


class NiveauResilience(Enum):
    """Niveaux de résilience du système selon la doctrine TPD"""
    SOUVERAIN = "souverain"        # Pleine maîtrise et autonomie
    RESILIENT = "résilient"        # Capacité d'adaptation élevée
    ADAPTATIF = "adaptatif"        # Réactivité contrôlée
    VULNERA = "vulnérable"         # Fragilité manifeste
    CRITIQUE = "critique"          # Effondrement imminent


class EtatPolyvagal(ABC):
    """
    Classe abstraite représentant un état polyvagal dans l'architecture TPD.
    
    Chaque état encode une stratégie neuro-numérique spécifique pour 
    la gestion de la résilience et de la souveraineté des systèmes.
    """
    
    def __init__(self, nom: str, niveau_resilience: NiveauResilience):
        self.nom = nom
        self.niveau_resilience = niveau_resilience
        self.timestamp_activation = datetime.now()
        self.metadata_contextuel: Dict[str, Any] = {}
        self.transitions_permises: List[str] = []
    
    @abstractmethod
    def evaluer_conscience_situationnelle(self, contexte: Dict[str, Any]) -> float:
        """
        Évalue le niveau de conscience situationnelle selon cet état.
        
        Returns:
            float: Score de conscience entre 0.0 (inconscience) et 1.0 (pleine conscience)
        """
        pass
    
    @abstractmethod
    def calculer_strategie_resilience(self, perturbations: List[Dict]) -> Dict[str, Any]:
        """
        Calcule la stratégie de résilience appropriée pour cet état.
        
        Args:
            perturbations: Liste des perturbations détectées dans le système
            
        Returns:
            Dict: Stratégie de résilience avec actions et priorités
        """
        pass
    
    @abstractmethod
    def determiner_transition_necessaire(self, contexte: Dict[str, Any]) -> Optional[str]:
        """
        Détermine si une transition vers un autre état est nécessaire.
        
        Returns:
            Optional[str]: Nom de l'état cible ou None si aucune transition
        """
        pass
    
    def activer(self, contexte: Dict[str, Any] = None):
        """Active cet état polyvagal avec le contexte donné."""
        self.timestamp_activation = datetime.now()
        if contexte:
            self.metadata_contextuel.update(contexte)
    
    def obtenir_diagnostic(self) -> Dict[str, Any]:
        """Retourne un diagnostic complet de l'état actuel."""
        return {
            "etat": self.nom,
            "niveau_resilience": self.niveau_resilience.value,
            "timestamp_activation": self.timestamp_activation.isoformat(),
            "duree_activation": (datetime.now() - self.timestamp_activation).total_seconds(),
            "metadata": self.metadata_contextuel,
            "transitions_permises": self.transitions_permises
        }


class EtatVentral(EtatPolyvagal):
    """
    État VENTRAL - Sécurité et Engagement Social
    ============================================
    
    L'état de fonctionnement optimal où le système manifeste :
    - Sécurité ontologique et confiance
    - Engagement social et collaboration
    - Innovation et créativité
    - Résilience proactive
    """
    
    def __init__(self):
        super().__init__(
            nom="VENTRAL",
            niveau_resilience=NiveauResilience.SOUVERAIN
        )
        self.transitions_permises = ["SYMPATHETIC", "DORSAL"]
        self.seuil_securite = 0.8
        self.capacite_innovation = 1.0
    
    def evaluer_conscience_situationnelle(self, contexte: Dict[str, Any]) -> float:
        """
        En état VENTRAL, la conscience situationnelle est maximale.
        Le système perçoit clairement son environnement et ses capacités.
        """
        facteurs_conscience = [
            contexte.get("stabilite_reseau", 1.0),
            contexte.get("qualite_donnees", 1.0), 
            contexte.get("coherence_systeme", 1.0),
            contexte.get("engagement_utilisateurs", 1.0)
        ]
        return sum(facteurs_conscience) / len(facteurs_conscience)
    
    def calculer_strategie_resilience(self, perturbations: List[Dict]) -> Dict[str, Any]:
        """
        Stratégie proactive de résilience basée sur l'anticipation et l'innovation.
        """
        return {
            "approche": "proactive",
            "priorite": "innovation_preventive",
            "actions": [
                "renforcement_capacites",
                "exploration_opportunites", 
                "optimisation_collaborative",
                "veille_strategique"
            ],
            "ressources_allouees": 0.3,  # 30% des ressources pour l'innovation
            "horizon_temporel": "long_terme"
        }
    
    def determiner_transition_necessaire(self, contexte: Dict[str, Any]) -> Optional[str]:
        """
        Transition vers SYMPATHETIC si menaces détectées,
        vers DORSAL si effondrement systémique imminent.
        """
        niveau_menace = contexte.get("niveau_menace", 0.0)
        charge_systeme = contexte.get("charge_systeme", 0.0)
        
        if charge_systeme > 0.9 or contexte.get("effondrement_detecte", False):
            return "DORSAL"
        elif niveau_menace > self.seuil_securite:
            return "SYMPATHETIC"
        
        return None


class EtatSympathetic(EtatPolyvagal):
    """
    État SYMPATHETIC - Mobilisation et Activation
    =============================================
    
    L'état de réponse adaptative où le système manifeste :
    - Mobilisation des ressources
    - Vigilance et réactivité accrues
    - Focus sur la performance
    - Gestion des défis et obstacles
    """
    
    def __init__(self):
        super().__init__(
            nom="SYMPATHETIC",
            niveau_resilience=NiveauResilience.ADAPTATIF
        )
        self.transitions_permises = ["VENTRAL", "DORSAL"]
        self.seuil_epuisement = 0.2
        self.multiplicateur_performance = 1.5
    
    def evaluer_conscience_situationnelle(self, contexte: Dict[str, Any]) -> float:
        """
        En état SYMPATHETIC, la conscience est focalisée sur les menaces.
        Perception sélective mais intense des défis.
        """
        facteurs_menace = [
            contexte.get("detection_anomalies", 0.5),
            contexte.get("pression_temporelle", 0.5),
            contexte.get("complexite_defis", 0.5)
        ]
        conscience_focalisee = sum(facteurs_menace) / len(facteurs_menace)
        return min(0.8, conscience_focalisee * 1.2)  # Plafonné à 0.8
    
    def calculer_strategie_resilience(self, perturbations: List[Dict]) -> Dict[str, Any]:
        """
        Stratégie réactive de mobilisation et de gestion des défis.
        """
        niveau_urgence = len(perturbations) / 10.0  # Normalisation
        
        return {
            "approche": "reactive",
            "priorite": "performance_immediate",
            "actions": [
                "mobilisation_ressources",
                "optimisation_performance",
                "gestion_urgences",
                "surveillance_continue"
            ],
            "ressources_allouees": min(0.8, 0.5 + niveau_urgence),
            "horizon_temporel": "court_terme"
        }
    
    def determiner_transition_necessaire(self, contexte: Dict[str, Any]) -> Optional[str]:
        """
        Transition vers VENTRAL si stabilisation réussie,
        vers DORSAL si épuisement ou surcharge critique.
        """
        ressources_disponibles = contexte.get("ressources_disponibles", 1.0)
        stabilite = contexte.get("stabilite_systeme", 0.5)
        
        if ressources_disponibles < self.seuil_epuisement:
            return "DORSAL"
        elif stabilite > 0.8 and contexte.get("menaces_resolues", False):
            return "VENTRAL"
        
        return None


class EtatDorsal(EtatPolyvagal):
    """
    État DORSAL - Conservation et Protection
    =======================================
    
    L'état de préservation où le système manifeste :
    - Conservation des ressources critiques
    - Protection des fonctions essentielles
    - Mode de survie et récupération
    - Résilience défensive
    """
    
    def __init__(self):
        super().__init__(
            nom="DORSAL",
            niveau_resilience=NiveauResilience.CRITIQUE
        )
        self.transitions_permises = ["SYMPATHETIC", "VENTRAL"]
        self.seuil_recuperation = 0.6
        self.ratio_conservation = 0.1  # Ne garde que 10% des fonctions
    
    def evaluer_conscience_situationnelle(self, contexte: Dict[str, Any]) -> float:
        """
        En état DORSAL, la conscience est réduite au minimum vital.
        Focus uniquement sur la survie et les fonctions critiques.
        """
        fonctions_critiques = contexte.get("fonctions_critiques_actives", 0.1)
        return max(0.1, fonctions_critiques)  # Minimum vital de conscience
    
    def calculer_strategie_resilience(self, perturbations: List[Dict]) -> Dict[str, Any]:
        """
        Stratégie défensive de conservation et de protection minimale.
        """
        return {
            "approche": "defensive",
            "priorite": "conservation_critique",
            "actions": [
                "arret_fonctions_non_essentielles",
                "preservation_donnees_critiques",
                "mode_degraded_controle",
                "preparation_recuperation"
            ],
            "ressources_allouees": self.ratio_conservation,
            "horizon_temporel": "immediat"
        }
    
    def determiner_transition_necessaire(self, contexte: Dict[str, Any]) -> Optional[str]:
        """
        Transition vers SYMPATHETIC si ressources suffisantes pour réactivation,
        vers VENTRAL si récupération complète possible.
        """
        ressources_disponibles = contexte.get("ressources_disponibles", 0.0)
        stabilite_retablie = contexte.get("stabilite_retablie", False)
        
        if ressources_disponibles > 0.8 and stabilite_retablie:
            return "VENTRAL"
        elif ressources_disponibles > self.seuil_recuperation:
            return "SYMPATHETIC"
        
        return None