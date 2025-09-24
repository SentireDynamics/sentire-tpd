"""
Conscience Situationnelle - Perception Neuro-Numérique
======================================================

Implémentation de la conscience situationnelle selon la doctrine TPD.
La conscience représente la capacité du système à percevoir, comprendre
et anticiper son environnement selon les états polyvagaux.
"""

from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime, timedelta
from dataclasses import dataclass, field
from enum import Enum
import math


class NiveauConscience(Enum):
    """Niveaux de conscience situationnelle selon la doctrine TPD."""
    INCONSCIENT = "inconscient"          # Aucune perception
    REACTIF = "reactif"                  # Perception immédiate seulement
    CONSCIENT = "conscient"              # Perception contextuelle
    VIGILANT = "vigilant"                # Perception anticipative
    OMNISCIENT = "omniscient"            # Perception holistique


@dataclass
class PerceptionSensorielle:
    """Représente une perception sensorielle du système."""
    timestamp: datetime
    source: str
    type_signal: str
    intensite: float  # 0.0 à 1.0
    fiabilite: float  # 0.0 à 1.0
    contexte: Dict[str, Any] = field(default_factory=dict)
    tags: List[str] = field(default_factory=list)


@dataclass
class PatternRecognition:
    """Représente un pattern reconnu dans l'environnement."""
    nom_pattern: str
    probabilite: float
    elements_constitutifs: List[str]
    implications_potentielles: List[str]
    niveau_certitude: float
    temporalite: str  # "passe", "present", "futur"


class ConscienceSituationnelle:
    """
    Conscience Situationnelle TPD
    ============================
    
    Système de perception et d'analyse contextuelle permettant au système
    de maintenir une conscience adaptée à son état polyvagal et aux 
    exigences de souveraineté numérique.
    """
    
    def __init__(self, nom: str = "ConscienceSituationnelle"):
        self.nom = nom
        self.niveau_conscience_actuel = NiveauConscience.CONSCIENT
        self.perceptions_actives: List[PerceptionSensorielle] = []
        self.patterns_reconnus: List[PatternRecognition] = []
        self.memoire_contextuelle: Dict[str, Any] = {}
        self.seuils_attention = {
            "critique": 0.9,
            "important": 0.7,
            "normal": 0.4,
            "negligeable": 0.1
        }
        self.horizon_temporel = timedelta(hours=24)
        self.capacite_traitement = 1.0
    
    def percevoir_environnement(self, signaux: List[Dict[str, Any]]) -> List[PerceptionSensorielle]:
        """
        Traite les signaux environnementaux pour créer des perceptions.
        
        Args:
            signaux: Liste des signaux bruts à traiter
            
        Returns:
            List[PerceptionSensorielle]: Perceptions structurées
        """
        perceptions = []
        
        for signal in signaux:
            # Filtrage selon la capacité de traitement actuelle
            if len(self.perceptions_actives) >= self.capacite_traitement * 100:
                break
            
            # Évaluation de l'intensité et de la fiabilité
            intensite = self._evaluer_intensite_signal(signal)
            fiabilite = self._evaluer_fiabilite_signal(signal)
            
            # Création de la perception si suffisamment significative
            if intensite > self.seuils_attention["negligeable"]:
                perception = PerceptionSensorielle(
                    timestamp=datetime.now(),
                    source=signal.get("source", "inconnu"),
                    type_signal=signal.get("type", "generique"),
                    intensite=intensite,
                    fiabilite=fiabilite,
                    contexte=signal.get("contexte", {}),
                    tags=self._generer_tags_perception(signal)
                )
                perceptions.append(perception)
        
        # Mise à jour des perceptions actives
        self.perceptions_actives.extend(perceptions)
        self._nettoyer_perceptions_obsoletes()
        
        return perceptions
    
    def analyser_patterns_emergents(self) -> List[PatternRecognition]:
        """
        Analyse les perceptions pour identifier des patterns émergents.
        
        Returns:
            List[PatternRecognition]: Patterns identifiés
        """
        patterns_detectes = []
        
        # Groupement des perceptions par type et temporalité
        groupes_temporels = self._grouper_perceptions_temporellement()
        
        for periode, perceptions_groupe in groupes_temporels.items():
            # Détection de patterns de fréquence
            pattern_frequence = self._detecter_pattern_frequence(perceptions_groupe)
            if pattern_frequence:
                patterns_detectes.append(pattern_frequence)
            
            # Détection de patterns d'intensité
            pattern_intensite = self._detecter_pattern_intensite(perceptions_groupe)
            if pattern_intensite:
                patterns_detectes.append(pattern_intensite)
            
            # Détection de patterns de corrélation
            patterns_correlation = self._detecter_patterns_correlation(perceptions_groupe)
            patterns_detectes.extend(patterns_correlation)
        
        # Mise à jour des patterns reconnus
        self.patterns_reconnus = patterns_detectes
        
        return patterns_detectes
    
    def evaluer_contexte_global(self, etat_polyvagal: str) -> Dict[str, Any]:
        """
        Évalue le contexte global selon l'état polyvagal actuel.
        
        Args:
            etat_polyvagal: État polyvagal actuel ("VENTRAL", "SYMPATHETIC", "DORSAL")
            
        Returns:
            Dict: Évaluation contextuelle complète
        """
        # Adaptation du niveau de conscience selon l'état polyvagal
        self._adapter_niveau_conscience(etat_polyvagal)
        
        contexte = {
            "timestamp": datetime.now(),
            "niveau_conscience": self.niveau_conscience_actuel.value,
            "etat_polyvagal": etat_polyvagal,
            "qualite_perception": self._calculer_qualite_perception(),
            "coherence_contextuelle": self._evaluer_coherence_contextuelle(),
            "niveau_menace_percu": self._evaluer_niveau_menace(),
            "opportunites_detectees": self._identifier_opportunites(),
            "stabilite_environnementale": self._evaluer_stabilite_environnement(),
            "predictibilite": self._calculer_predictibilite(),
            "recommandations": self._generer_recommandations_contextuelles()
        }
        
        # Mise à jour de la mémoire contextuelle
        self.memoire_contextuelle[datetime.now().isoformat()] = contexte
        self._maintenir_memoire_contextuelle()
        
        return contexte
    
    def anticiper_evolutions(self, horizon: timedelta = None) -> Dict[str, Any]:
        """
        Anticipe les évolutions probables de l'environnement.
        
        Args:
            horizon: Horizon temporel d'anticipation
            
        Returns:
            Dict: Prédictions et recommandations
        """
        if horizon is None:
            horizon = self.horizon_temporel
        
        # Analyse des tendances historiques
        tendances = self._analyser_tendances_historiques()
        
        # Projection des patterns identifiés
        projections = self._projeter_patterns_futurs(horizon)
        
        # Évaluation des scénarios probables
        scenarios = self._evaluer_scenarios_probables(tendances, projections)
        
        return {
            "horizon_anticipation": horizon.total_seconds(),
            "tendances_identifiees": tendances,
            "projections_patterns": projections,
            "scenarios_probables": scenarios,
            "actions_recommandees": self._recommander_actions_anticipatives(scenarios),
            "niveau_incertitude": self._calculer_niveau_incertitude(),
            "confiance_predictions": self._evaluer_confiance_predictions()
        }
    
    # Méthodes privées pour l'implémentation interne
    
    def _evaluer_intensite_signal(self, signal: Dict[str, Any]) -> float:
        """Évalue l'intensité d'un signal selon les critères TPD."""
        facteurs = [
            signal.get("amplitude", 0.5),
            signal.get("urgence", 0.5),
            signal.get("impact_potentiel", 0.5),
            signal.get("pertinence_contextuelle", 0.5)
        ]
        return sum(facteurs) / len(facteurs)
    
    def _evaluer_fiabilite_signal(self, signal: Dict[str, Any]) -> float:
        """Évalue la fiabilité d'un signal."""
        facteurs_fiabilite = [
            signal.get("source_credibilite", 0.8),
            signal.get("coherence_interne", 0.8),
            signal.get("verification_croisee", 0.6),
            signal.get("historique_source", 0.7)
        ]
        return sum(facteurs_fiabilite) / len(facteurs_fiabilite)
    
    def _generer_tags_perception(self, signal: Dict[str, Any]) -> List[str]:
        """Génère des tags pour catégoriser la perception."""
        tags = []
        
        if signal.get("urgence", 0) > 0.8:
            tags.append("urgent")
        if signal.get("impact_potentiel", 0) > 0.7:
            tags.append("impact_significatif")
        if signal.get("anomalie", False):
            tags.append("anomalie")
        if signal.get("opportunite", False):
            tags.append("opportunite")
        
        return tags
    
    def _nettoyer_perceptions_obsoletes(self):
        """Supprime les perceptions trop anciennes."""
        seuil_obsolescence = datetime.now() - self.horizon_temporel
        self.perceptions_actives = [
            p for p in self.perceptions_actives 
            if p.timestamp > seuil_obsolescence
        ]
    
    def _grouper_perceptions_temporellement(self) -> Dict[str, List[PerceptionSensorielle]]:
        """Groupe les perceptions par tranches temporelles."""
        maintenant = datetime.now()
        groupes = {
            "immediat": [],     # Dernières 5 minutes
            "recent": [],       # Dernière heure
            "proche": [],       # Dernières 6 heures
            "distant": []       # Plus ancien
        }
        
        for perception in self.perceptions_actives:
            delta = maintenant - perception.timestamp
            
            if delta <= timedelta(minutes=5):
                groupes["immediat"].append(perception)
            elif delta <= timedelta(hours=1):
                groupes["recent"].append(perception)
            elif delta <= timedelta(hours=6):
                groupes["proche"].append(perception)
            else:
                groupes["distant"].append(perception)
        
        return groupes
    
    def _detecter_pattern_frequence(self, perceptions: List[PerceptionSensorielle]) -> Optional[PatternRecognition]:
        """Détecte des patterns basés sur la fréquence."""
        if len(perceptions) < 3:
            return None
        
        # Analyse de la fréquence des types de signaux
        types_signaux = {}
        for p in perceptions:
            types_signaux[p.type_signal] = types_signaux.get(p.type_signal, 0) + 1
        
        # Identification du pattern dominant
        if types_signaux:
            type_dominant = max(types_signaux, key=types_signaux.get)
            frequence = types_signaux[type_dominant] / len(perceptions)
            
            if frequence > 0.6:  # Pattern significatif
                return PatternRecognition(
                    nom_pattern=f"frequence_{type_dominant}",
                    probabilite=frequence,
                    elements_constitutifs=[type_dominant],
                    implications_potentielles=[f"Récurrence de {type_dominant}"],
                    niveau_certitude=frequence,
                    temporalite="present"
                )
        
        return None
    
    def _detecter_pattern_intensite(self, perceptions: List[PerceptionSensorielle]) -> Optional[PatternRecognition]:
        """Détecte des patterns basés sur l'intensité."""
        if len(perceptions) < 2:
            return None
        
        intensites = [p.intensite for p in perceptions]
        tendance = self._calculer_tendance(intensites)
        
        if abs(tendance) > 0.3:  # Tendance significative
            direction = "croissante" if tendance > 0 else "decroissante"
            return PatternRecognition(
                nom_pattern=f"intensite_{direction}",
                probabilite=abs(tendance),
                elements_constitutifs=["variation_intensite"],
                implications_potentielles=[f"Évolution {direction} de l'activité"],
                niveau_certitude=abs(tendance),
                temporalite="present"
            )
        
        return None
    
    def _detecter_patterns_correlation(self, perceptions: List[PerceptionSensorielle]) -> List[PatternRecognition]:
        """Détecte des patterns de corrélation entre signaux."""
        patterns = []
        
        # Analyse des corrélations temporelles entre types de signaux
        types_uniques = list(set(p.type_signal for p in perceptions))
        
        for i, type1 in enumerate(types_uniques):
            for type2 in types_uniques[i+1:]:
                correlation = self._calculer_correlation_temporelle(
                    perceptions, type1, type2
                )
                
                if correlation > 0.7:  # Corrélation forte
                    patterns.append(PatternRecognition(
                        nom_pattern=f"correlation_{type1}_{type2}",
                        probabilite=correlation,
                        elements_constitutifs=[type1, type2],
                        implications_potentielles=[f"Lien causal entre {type1} et {type2}"],
                        niveau_certitude=correlation,
                        temporalite="present"
                    ))
        
        return patterns
    
    def _adapter_niveau_conscience(self, etat_polyvagal: str):
        """Adapte le niveau de conscience selon l'état polyvagal."""
        if etat_polyvagal == "VENTRAL":
            self.niveau_conscience_actuel = NiveauConscience.VIGILANT
            self.capacite_traitement = 1.0
        elif etat_polyvagal == "SYMPATHETIC":
            self.niveau_conscience_actuel = NiveauConscience.CONSCIENT
            self.capacite_traitement = 0.8
        elif etat_polyvagal == "DORSAL":
            self.niveau_conscience_actuel = NiveauConscience.REACTIF
            self.capacite_traitement = 0.3
    
    def _calculer_qualite_perception(self) -> float:
        """Calcule la qualité globale de la perception."""
        if not self.perceptions_actives:
            return 0.0
        
        fiabilites = [p.fiabilite for p in self.perceptions_actives]
        return sum(fiabilites) / len(fiabilites)
    
    def _evaluer_coherence_contextuelle(self) -> float:
        """Évalue la cohérence du contexte perçu."""
        if len(self.perceptions_actives) < 2:
            return 1.0
        
        # Calcul basé sur la cohérence temporelle et thématique
        coherence_temporelle = self._calculer_coherence_temporelle()
        coherence_thematique = self._calculer_coherence_thematique()
        
        return (coherence_temporelle + coherence_thematique) / 2
    
    def _evaluer_niveau_menace(self) -> float:
        """Évalue le niveau de menace perçu."""
        if not self.perceptions_actives:
            return 0.0
        
        perceptions_menacantes = [
            p for p in self.perceptions_actives 
            if "urgent" in p.tags or "anomalie" in p.tags
        ]
        
        if not perceptions_menacantes:
            return 0.0
        
        intensites_menaces = [p.intensite for p in perceptions_menacantes]
        return max(intensites_menaces)
    
    def _identifier_opportunites(self) -> List[Dict[str, Any]]:
        """Identifie les opportunités dans les perceptions."""
        opportunites = []
        
        for perception in self.perceptions_actives:
            if "opportunite" in perception.tags:
                opportunites.append({
                    "type": perception.type_signal,
                    "potentiel": perception.intensite,
                    "fiabilite": perception.fiabilite,
                    "contexte": perception.contexte
                })
        
        return opportunites
    
    def _evaluer_stabilite_environnement(self) -> float:
        """Évalue la stabilité de l'environnement."""
        if len(self.perceptions_actives) < 5:
            return 0.8  # Stabilité par défaut si peu de données
        
        # Calcul basé sur la variance des intensités
        intensites = [p.intensite for p in self.perceptions_actives]
        variance = self._calculer_variance(intensites)
        
        # Stabilité inversement proportionnelle à la variance
        return max(0.0, 1.0 - variance)
    
    def _calculer_predictibilite(self) -> float:
        """Calcule la prévisibilité des patterns."""
        if not self.patterns_reconnus:
            return 0.5
        
        certitudes = [p.niveau_certitude for p in self.patterns_reconnus]
        return sum(certitudes) / len(certitudes)
    
    def _generer_recommandations_contextuelles(self) -> List[str]:
        """Génère des recommandations basées sur le contexte."""
        recommandations = []
        
        if self._evaluer_niveau_menace() > 0.7:
            recommandations.append("Activer protocoles de protection")
        
        if len(self._identifier_opportunites()) > 0:
            recommandations.append("Explorer opportunités détectées")
        
        if self._evaluer_stabilite_environnement() < 0.4:
            recommandations.append("Renforcer surveillance environnementale")
        
        if self._calculer_predictibilite() < 0.3:
            recommandations.append("Améliorer collecte de données")
        
        return recommandations
    
    # Méthodes utilitaires pour les calculs statistiques
    
    def _calculer_tendance(self, valeurs: List[float]) -> float:
        """Calcule la tendance d'une série de valeurs."""
        if len(valeurs) < 2:
            return 0.0
        
        # Régression linéaire simple
        n = len(valeurs)
        x = list(range(n))
        
        sum_x = sum(x)
        sum_y = sum(valeurs)
        sum_xy = sum(x[i] * valeurs[i] for i in range(n))
        sum_x2 = sum(xi * xi for xi in x)
        
        if n * sum_x2 - sum_x * sum_x == 0:
            return 0.0
        
        pente = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)
        return pente
    
    def _calculer_variance(self, valeurs: List[float]) -> float:
        """Calcule la variance d'une série de valeurs."""
        if len(valeurs) < 2:
            return 0.0
        
        moyenne = sum(valeurs) / len(valeurs)
        return sum((v - moyenne) ** 2 for v in valeurs) / len(valeurs)
    
    def _calculer_correlation_temporelle(self, perceptions: List[PerceptionSensorielle], 
                                       type1: str, type2: str) -> float:
        """Calcule la corrélation temporelle entre deux types de signaux."""
        # Implémentation simplifiée - dans un vrai système, utiliser des méthodes statistiques robustes
        perceptions_type1 = [p for p in perceptions if p.type_signal == type1]
        perceptions_type2 = [p for p in perceptions if p.type_signal == type2]
        
        if len(perceptions_type1) < 2 or len(perceptions_type2) < 2:
            return 0.0
        
        # Calcul basé sur la proximité temporelle des occurrences
        correlations = []
        for p1 in perceptions_type1:
            for p2 in perceptions_type2:
                delta_temps = abs((p1.timestamp - p2.timestamp).total_seconds())
                if delta_temps < 300:  # 5 minutes de fenêtre
                    correlations.append(1.0 - (delta_temps / 300))
        
        return sum(correlations) / len(correlations) if correlations else 0.0
    
    def _calculer_coherence_temporelle(self) -> float:
        """Calcule la cohérence temporelle des perceptions."""
        # Implémentation simplifiée
        return 0.8
    
    def _calculer_coherence_thematique(self) -> float:
        """Calcule la cohérence thématique des perceptions."""
        # Implémentation simplifiée
        return 0.7
    
    def _analyser_tendances_historiques(self) -> Dict[str, Any]:
        """Analyse les tendances dans l'historique."""
        return {"tendances": "analysis_placeholder"}
    
    def _projeter_patterns_futurs(self, horizon: timedelta) -> Dict[str, Any]:
        """Projette les patterns dans le futur."""
        return {"projections": "projection_placeholder"}
    
    def _evaluer_scenarios_probables(self, tendances: Dict, projections: Dict) -> List[Dict[str, Any]]:
        """Évalue les scénarios probables."""
        return [{"scenario": "scenario_placeholder"}]
    
    def _recommander_actions_anticipatives(self, scenarios: List[Dict]) -> List[str]:
        """Recommande des actions anticipatives."""
        return ["action_placeholder"]
    
    def _calculer_niveau_incertitude(self) -> float:
        """Calcule le niveau d'incertitude."""
        return 0.3
    
    def _evaluer_confiance_predictions(self) -> float:
        """Évalue la confiance dans les prédictions."""
        return 0.7
    
    def _maintenir_memoire_contextuelle(self):
        """Maintient la mémoire contextuelle en supprimant les anciens éléments."""
        seuil_memoire = datetime.now() - timedelta(days=7)
        self.memoire_contextuelle = {
            k: v for k, v in self.memoire_contextuelle.items()
            if datetime.fromisoformat(k) > seuil_memoire
        }