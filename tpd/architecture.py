"""
Architecture Guardian/Predator - Souveraineté Neuro-Numérique
==============================================================

Implémentation de l'architecture duale Guardian/Predator pour la protection
et l'adaptation dynamique des systèmes selon la doctrine TPD.

- Guardian : Protection, stabilité, préservation de l'intégrité
- Predator : Adaptation, exploration, expansion des capacités
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional, Callable
from datetime import datetime, timedelta
import logging
from dataclasses import dataclass
from .etats import EtatPolyvagal, EtatVentral, EtatSympathetic, EtatDorsal, NiveauResilience


@dataclass
class EvenementSysteme:
    """Représente un événement dans le système nécessitant une réponse."""
    timestamp: datetime
    type_evenement: str
    severite: str  # "info", "attention", "alerte", "critique"
    contexte: Dict[str, Any]
    source: str
    impact_prevu: float  # 0.0 à 1.0


class StrategieAdaptive(ABC):
    """Interface pour les stratégies adaptatives Guardian/Predator."""
    
    @abstractmethod
    def evaluer_pertinence(self, evenement: EvenementSysteme, contexte: Dict[str, Any]) -> float:
        """Évalue la pertinence de cette stratégie pour l'événement donné."""
        pass
    
    @abstractmethod
    def executer(self, evenement: EvenementSysteme, ressources: Dict[str, Any]) -> Dict[str, Any]:
        """Exécute la stratégie et retourne les résultats."""
        pass


class Guardian:
    """
    Guardian - Gardien de la Souveraineté
    =====================================
    
    Responsable de la protection, de la stabilité et de la préservation
    de l'intégrité du système. Agit selon les principes de conservation
    et de résilience défensive.
    """
    
    def __init__(self, nom: str = "Guardian"):
        self.nom = nom
        self.niveau_vigilance = 0.5
        self.seuils_protection = {
            "ressources_critiques": 0.2,
            "integrite_donnees": 0.9,
            "stabilite_systeme": 0.7
        }
        self.strategies_protection: List[StrategieAdaptive] = []
        self.historique_interventions: List[Dict[str, Any]] = []
        self.protocoles_urgence: Dict[str, Callable] = {}
    
    def evaluer_menaces(self, contexte: Dict[str, Any]) -> Dict[str, float]:
        """
        Évalue les menaces potentielles selon la doctrine de protection.
        
        Returns:
            Dict: Cartographie des menaces avec scores de risque
        """
        menaces_detectees = {}
        
        # Évaluation des ressources critiques
        if contexte.get("ressources_disponibles", 1.0) < self.seuils_protection["ressources_critiques"]:
            menaces_detectees["epuisement_ressources"] = 0.9
        
        # Évaluation de l'intégrité des données
        integrite = contexte.get("integrite_donnees", 1.0)
        if integrite < self.seuils_protection["integrite_donnees"]:
            menaces_detectees["corruption_donnees"] = 1.0 - integrite
        
        # Évaluation de la stabilité système
        stabilite = contexte.get("stabilite_systeme", 1.0)
        if stabilite < self.seuils_protection["stabilite_systeme"]:
            menaces_detectees["instabilite_systeme"] = 1.0 - stabilite
        
        # Détection d'anomalies comportementales
        if contexte.get("anomalies_detectees", 0) > 5:
            menaces_detectees["anomalies_comportement"] = min(1.0, contexte["anomalies_detectees"] / 10.0)
        
        return menaces_detectees
    
    def calculer_strategie_protection(self, menaces: Dict[str, float], 
                                    etat_actuel: EtatPolyvagal) -> Dict[str, Any]:
        """
        Calcule la stratégie de protection optimale selon l'état polyvagal.
        """
        if not menaces:
            return {"niveau_protection": "minimal", "actions": []}
        
        niveau_menace_max = max(menaces.values())
        
        if isinstance(etat_actuel, EtatDorsal):
            # En mode DORSAL, protection maximale
            return {
                "niveau_protection": "maximal",
                "actions": [
                    "isolation_fonctions_critiques",
                    "sauvegarde_donnees_essentielles", 
                    "activation_mode_survie",
                    "notification_urgence_administrateurs"
                ],
                "ressources_allouees": 0.9,
                "duree_protection": "indefinie"
            }
        elif isinstance(etat_actuel, EtatSympathetic):
            # En mode SYMPATHETIC, protection active
            return {
                "niveau_protection": "actif",
                "actions": [
                    "renforcement_monitoring",
                    "isolation_preventive_zones_risque",
                    "acceleration_reponses_securite",
                    "mobilisation_ressources_protection"
                ],
                "ressources_allouees": 0.6,
                "duree_protection": "temporaire_adaptatif"
            }
        else:  # EtatVentral
            # En mode VENTRAL, protection collaborative
            return {
                "niveau_protection": "collaboratif",
                "actions": [
                    "analyse_proactive_risques",
                    "renforcement_resilience_collective",
                    "optimisation_defenses_naturelles",
                    "education_prevention_communaute"
                ],
                "ressources_allouees": 0.3,
                "duree_protection": "continue_adaptative"
            }
    
    def executer_protection(self, strategie: Dict[str, Any], contexte: Dict[str, Any]) -> Dict[str, Any]:
        """Exécute la stratégie de protection calculée."""
        intervention = {
            "timestamp": datetime.now(),
            "strategie": strategie,
            "contexte": contexte.copy(),
            "guardian": self.nom,
            "resultats": {}
        }
        
        # Simulation d'exécution des actions de protection
        for action in strategie.get("actions", []):
            intervention["resultats"][action] = {
                "statut": "execute",
                "efficacite": 0.8,  # Simulation
                "ressources_utilisees": strategie.get("ressources_allouees", 0.3) / len(strategie["actions"])
            }
        
        self.historique_interventions.append(intervention)
        return intervention


class Predator:
    """
    Predator - Catalyseur d'Adaptation
    ==================================
    
    Responsable de l'adaptation, de l'exploration et de l'expansion
    des capacités du système. Agit selon les principes d'innovation
    et de résilience offensive.
    """
    
    def __init__(self, nom: str = "Predator"):
        self.nom = nom
        self.niveau_agressivite = 0.5
        self.seuils_opportunite = {
            "ressources_disponibles": 0.6,
            "stabilite_requise": 0.8,
            "potentiel_innovation": 0.3
        }
        self.strategies_expansion: List[StrategieAdaptive] = []
        self.historique_adaptations: List[Dict[str, Any]] = []
        self.protocoles_exploration: Dict[str, Callable] = {}
    
    def detecter_opportunites(self, contexte: Dict[str, Any]) -> Dict[str, float]:
        """
        Détecte les opportunités d'adaptation et d'expansion.
        
        Returns:
            Dict: Cartographie des opportunités avec scores de potentiel
        """
        opportunites = {}
        
        # Détection d'opportunités d'optimisation
        efficacite_actuelle = contexte.get("efficacite_systeme", 0.7)
        if efficacite_actuelle < 0.9:
            opportunites["optimisation_performance"] = 0.9 - efficacite_actuelle
        
        # Détection d'opportunités d'expansion
        ressources_excedentaires = contexte.get("ressources_disponibles", 0.5) - 0.3
        if ressources_excedentaires > 0:
            opportunites["expansion_capacites"] = min(1.0, ressources_excedentaires * 2)
        
        # Détection d'opportunités d'innovation
        if contexte.get("donnees_nouvelles", 0) > 100:
            opportunites["innovation_algorithmique"] = min(1.0, contexte["donnees_nouvelles"] / 1000)
        
        # Détection d'opportunités collaboratives
        if contexte.get("demandes_collaboration", 0) > 0:
            opportunites["expansion_collaborative"] = min(1.0, contexte["demandes_collaboration"] / 10)
        
        return opportunites
    
    def calculer_strategie_adaptation(self, opportunites: Dict[str, float],
                                    etat_actuel: EtatPolyvagal) -> Dict[str, Any]:
        """
        Calcule la stratégie d'adaptation optimale selon l'état polyvagal.
        """
        if not opportunites:
            return {"niveau_adaptation": "minimal", "actions": []}
        
        potentiel_max = max(opportunites.values()) if opportunites else 0
        
        if isinstance(etat_actuel, EtatVentral):
            # En mode VENTRAL, adaptation créative maximale
            return {
                "niveau_adaptation": "creatif",
                "actions": [
                    "exploration_possibilites_emergentes",
                    "innovation_collaborative",
                    "expansion_capacites_resilience",
                    "creation_nouvelles_connexions"
                ],
                "ressources_allouees": 0.4,
                "horizon_adaptation": "long_terme_visionnnaire"
            }
        elif isinstance(etat_actuel, EtatSympathetic):
            # En mode SYMPATHETIC, adaptation tactique
            return {
                "niveau_adaptation": "tactique", 
                "actions": [
                    "optimisation_performance_immediate",
                    "adaptation_reactive_defis",
                    "mobilisation_efficacite",
                    "exploitation_opportunites_imediates"
                ],
                "ressources_allouees": 0.3,
                "horizon_adaptation": "court_terme_efficace"
            }
        else:  # EtatDorsal
            # En mode DORSAL, adaptation minimale de survie
            return {
                "niveau_adaptation": "survie",
                "actions": [
                    "preservation_capacites_essentielles",
                    "adaptation_minimale_necessaire",
                    "preparation_recuperation_future"
                ],
                "ressources_allouees": 0.1,
                "horizon_adaptation": "immediat_conservateur"
            }
    
    def executer_adaptation(self, strategie: Dict[str, Any], contexte: Dict[str, Any]) -> Dict[str, Any]:
        """Exécute la stratégie d'adaptation calculée."""
        adaptation = {
            "timestamp": datetime.now(),
            "strategie": strategie,
            "contexte": contexte.copy(),
            "predator": self.nom,
            "resultats": {}
        }
        
        # Simulation d'exécution des actions d'adaptation
        for action in strategie.get("actions", []):
            adaptation["resultats"][action] = {
                "statut": "execute",
                "innovation": 0.7,  # Simulation
                "ressources_utilisees": strategie.get("ressources_allouees", 0.3) / len(strategie["actions"])
            }
        
        self.historique_adaptations.append(adaptation)
        return adaptation


class SystemeResilience:
    """
    Système de Résilience TPD - Orchestrateur Guardian/Predator
    ===========================================================
    
    Orchestre la collaboration entre Guardian et Predator pour maintenir
    la souveraineté et la résilience du système selon la doctrine TPD.
    """
    
    def __init__(self, nom: str = "SystemeResilience"):
        self.nom = nom
        self.etat_actuel: EtatPolyvagal = EtatVentral()
        self.guardian = Guardian(f"{nom}_Guardian")
        self.predator = Predator(f"{nom}_Predator")
        self.historique_etats: List[Dict[str, Any]] = []
        self.metriques_souverainete: Dict[str, float] = {}
        self.seuils_transition = {
            "ventral_vers_sympathetic": 0.6,
            "sympathetic_vers_dorsal": 0.8,
            "dorsal_vers_sympathetic": 0.4,
            "sympathetic_vers_ventral": 0.3
        }
    
    def evaluer_contexte_systemique(self, evenements: List[EvenementSysteme]) -> Dict[str, Any]:
        """
        Évalue le contexte systémique global à partir des événements.
        """
        contexte = {
            "timestamp": datetime.now(),
            "nombre_evenements": len(evenements),
            "niveau_menace": 0.0,
            "opportunites_detectees": 0,
            "ressources_disponibles": 1.0,
            "stabilite_systeme": 1.0,
            "efficacite_systeme": 0.8
        }
        
        # Analyse des événements pour construire le contexte
        if evenements:
            severites = [ev.impact_prevu for ev in evenements]
            contexte["niveau_menace"] = max(severites)
            contexte["niveau_stress"] = sum(severites) / len(severites)
            
            # Compter les types d'événements
            critiques = sum(1 for ev in evenements if ev.severite == "critique")
            alertes = sum(1 for ev in evenements if ev.severite == "alerte")
            
            if critiques > 0:
                contexte["ressources_disponibles"] = max(0.1, 1.0 - (critiques * 0.3))
                contexte["stabilite_systeme"] = max(0.2, 1.0 - (critiques * 0.4))
            elif alertes > 2:
                contexte["ressources_disponibles"] = max(0.3, 1.0 - (alertes * 0.1))
                contexte["stabilite_systeme"] = max(0.5, 1.0 - (alertes * 0.2))
        
        return contexte
    
    def gerer_cycle_polyvagal(self, contexte: Dict[str, Any]) -> Optional[EtatPolyvagal]:
        """
        Gère les transitions entre états polyvagaux selon le contexte.
        """
        transition_necessaire = self.etat_actuel.determiner_transition_necessaire(contexte)
        
        if transition_necessaire:
            nouvel_etat = None
            
            if transition_necessaire == "VENTRAL":
                nouvel_etat = EtatVentral()
            elif transition_necessaire == "SYMPATHETIC":
                nouvel_etat = EtatSympathetic()
            elif transition_necessaire == "DORSAL":
                nouvel_etat = EtatDorsal()
            
            if nouvel_etat:
                # Enregistrer la transition
                self.historique_etats.append({
                    "timestamp": datetime.now(),
                    "etat_precedent": self.etat_actuel.nom,
                    "nouvel_etat": nouvel_etat.nom,
                    "contexte_transition": contexte.copy(),
                    "justification": f"Transition automatique selon seuils TPD"
                })
                
                self.etat_actuel = nouvel_etat
                self.etat_actuel.activer(contexte)
                
                return nouvel_etat
        
        return None
    
    def orchestrer_resilience(self, evenements: List[EvenementSysteme]) -> Dict[str, Any]:
        """
        Orchestre la réponse Guardian/Predator selon l'état polyvagal actuel.
        """
        contexte = self.evaluer_contexte_systemique(evenements)
        
        # Gérer les transitions d'état si nécessaire
        transition = self.gerer_cycle_polyvagal(contexte)
        
        # Orchestrer Guardian (protection)
        menaces = self.guardian.evaluer_menaces(contexte)
        strategie_protection = self.guardian.calculer_strategie_protection(menaces, self.etat_actuel)
        intervention_guardian = self.guardian.executer_protection(strategie_protection, contexte)
        
        # Orchestrer Predator (adaptation)
        opportunites = self.predator.detecter_opportunites(contexte)
        strategie_adaptation = self.predator.calculer_strategie_adaptation(opportunites, self.etat_actuel)
        adaptation_predator = self.predator.executer_adaptation(strategie_adaptation, contexte)
        
        # Calculer métriques de souveraineté
        self.metriques_souverainete = self._calculer_metriques_souverainete(
            contexte, intervention_guardian, adaptation_predator
        )
        
        return {
            "timestamp": datetime.now(),
            "etat_polyvagal": self.etat_actuel.nom,
            "transition_effectuee": transition.nom if transition else None,
            "contexte_systemique": contexte,
            "intervention_guardian": intervention_guardian,
            "adaptation_predator": adaptation_predator,
            "metriques_souverainete": self.metriques_souverainete,
            "diagnostic_complet": self.obtenir_diagnostic_complet()
        }
    
    def _calculer_metriques_souverainete(self, contexte: Dict[str, Any], 
                                       intervention: Dict[str, Any],
                                       adaptation: Dict[str, Any]) -> Dict[str, float]:
        """Calcule les métriques de souveraineté du système."""
        return {
            "autonomie": contexte.get("ressources_disponibles", 0.5),
            "resilience": self.etat_actuel.niveau_resilience.value == "souverain" and 1.0 or 0.6,
            "adaptabilite": len(adaptation.get("resultats", {})) / 5.0,
            "protection": len(intervention.get("resultats", {})) / 5.0,
            "conscience_situationnelle": self.etat_actuel.evaluer_conscience_situationnelle(contexte),
            "souverainete_globale": 0.0  # Calculé comme moyenne pondérée
        }
    
    def obtenir_diagnostic_complet(self) -> Dict[str, Any]:
        """Retourne un diagnostic complet du système de résilience."""
        return {
            "systeme": self.nom,
            "etat_polyvagal_actuel": self.etat_actuel.obtenir_diagnostic(),
            "guardian_status": {
                "interventions_recentes": len(self.guardian.historique_interventions),
                "niveau_vigilance": self.guardian.niveau_vigilance
            },
            "predator_status": {
                "adaptations_recentes": len(self.predator.historique_adaptations),
                "niveau_agressivite": self.predator.niveau_agressivite
            },
            "historique_transitions": len(self.historique_etats),
            "metriques_souverainete": self.metriques_souverainete
        }