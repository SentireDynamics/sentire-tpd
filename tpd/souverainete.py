"""
Souveraineté Numérique - Autonomie et Autodétermination Systémique
==================================================================

Implémentation de la souveraineté numérique selon la doctrine TPD.
La souveraineté représente la capacité du système à maintenir son 
autodétermination, son autonomie et sa résistance aux influences externes.
"""

from typing import Dict, Any, List, Optional, Set, Tuple
from datetime import datetime, timedelta
from dataclasses import dataclass, field
from enum import Enum
import uuid


class NiveauSouverainete(Enum):
    """Niveaux de souveraineté numérique selon la doctrine TPD."""
    ASSUJETTI = "assujetti"              # Dépendance externe totale
    DEPENDANT = "dependant"              # Dépendance externe partielle
    AUTONOME = "autonome"                # Autonomie fonctionnelle
    SOUVERAIN = "souverain"              # Souveraineté complète
    HEGEMONE = "hegemone"                # Influence sur d'autres systèmes


class DomaineSouverainete(Enum):
    """Domaines de la souveraineté numérique."""
    DONNEES = "donnees"                  # Contrôle des données
    ALGORITHMES = "algorithmes"          # Contrôle algorithmique
    INFRASTRUCTURE = "infrastructure"    # Contrôle infrastructurel
    COMMUNICATION = "communication"      # Contrôle communicationnel
    DECISION = "decision"                # Autonomie décisionnelle
    RESSOURCES = "ressources"            # Contrôle des ressources


@dataclass
class MetriqueSouverainete:
    """Métrique de souveraineté pour un domaine spécifique."""
    domaine: DomaineSouverainete
    niveau: float  # 0.0 (assujettissement) à 1.0 (souveraineté complète)
    facteurs_contributifs: List[str] = field(default_factory=list)
    dependances_externes: List[str] = field(default_factory=list)
    capacites_internes: List[str] = field(default_factory=list)
    vulnerabilites: List[str] = field(default_factory=list)
    timestamp: datetime = field(default_factory=datetime.now)


@dataclass
class DependanceExterne:
    """Représente une dépendance externe qui affecte la souveraineté."""
    id_dependance: str
    nom: str
    type_dependance: str  # "critique", "importante", "optionnelle"
    domaine: DomaineSouverainete
    niveau_criticite: float  # 0.0 à 1.0
    alternatives_disponibles: List[str] = field(default_factory=list)
    cout_elimination: float = 0.0
    risque_rupture: float = 0.0
    impact_souverainete: float = 0.0


@dataclass
class CapaciteInterne:
    """Représente une capacité interne qui renforce la souveraineté."""
    id_capacite: str
    nom: str
    domaine: DomaineSouverainete
    niveau_maturite: float  # 0.0 à 1.0
    autonomie_conferee: float  # 0.0 à 1.0
    cout_maintenance: float = 0.0
    potentiel_evolution: float = 0.0
    synergies: List[str] = field(default_factory=list)


class SouveraineteNumerique:
    """
    Souveraineté Numérique TPD
    ==========================
    
    Système de gestion et d'optimisation de la souveraineté numérique
    permettant au système de maintenir son autodétermination et sa 
    résistance aux influences externes selon la doctrine TPD.
    """
    
    def __init__(self, nom: str = "SouveraineteNumerique"):
        self.nom = nom
        self.niveau_souverainete_global = NiveauSouverainete.AUTONOME
        self.metriques_domaines: Dict[DomaineSouverainete, MetriqueSouverainete] = {}
        self.dependances_externes: Dict[str, DependanceExterne] = {}
        self.capacites_internes: Dict[str, CapaciteInterne] = {}
        self.historique_souverainete: List[Dict[str, Any]] = []
        self.seuils_criticite = {
            "assujettissement": 0.2,
            "dependance": 0.4,
            "autonomie": 0.6,
            "souverainete": 0.8,
            "hegemonie": 0.95
        }
        self.strategie_souverainete: Dict[str, Any] = {}
        
        # Initialisation des métriques par domaine
        self._initialiser_metriques_domaines()
    
    def evaluer_souverainete_globale(self, contexte: Dict[str, Any]) -> Dict[str, Any]:
        """
        Évalue la souveraineté globale du système.
        
        Args:
            contexte: Contexte systémique actuel
            
        Returns:
            Dict: Évaluation complète de la souveraineté
        """
        # Mise à jour des métriques par domaine
        for domaine in DomaineSouverainete:
            self._evaluer_souverainete_domaine(domaine, contexte)
        
        # Calcul du niveau global
        niveau_global = self._calculer_niveau_global()
        self.niveau_souverainete_global = self._determiner_niveau_souverainete(niveau_global)
        
        # Analyse des vulnérabilités et opportunités
        vulnerabilites = self._identifier_vulnerabilites_souverainete()
        opportunites = self._identifier_opportunites_souverainete()
        
        # Génération de la stratégie
        self.strategie_souverainete = self._generer_strategie_souverainete(
            vulnerabilites, opportunites, contexte
        )
        
        evaluation = {
            "timestamp": datetime.now(),
            "niveau_global": niveau_global,
            "classification": self.niveau_souverainete_global.value,
            "metriques_domaines": {
                domaine.value: {
                    "niveau": metrique.niveau,
                    "dependances": len(metrique.dependances_externes),
                    "capacites": len(metrique.capacites_internes),
                    "vulnerabilites": len(metrique.vulnerabilites)
                }
                for domaine, metrique in self.metriques_domaines.items()
            },
            "vulnerabilites_critiques": vulnerabilites,
            "opportunites_renforcement": opportunites,
            "strategie_recommandee": self.strategie_souverainete,
            "indice_resilience_souverainete": self._calculer_indice_resilience()
        }
        
        # Enregistrement dans l'historique
        self.historique_souverainete.append(evaluation)
        self._maintenir_historique()
        
        return evaluation
    
    def analyser_dependances_critiques(self) -> Dict[str, Any]:
        """
        Analyse les dépendances critiques qui affectent la souveraineté.
        
        Returns:
            Dict: Analyse détaillée des dépendances
        """
        dependances_critiques = {
            dep_id: dep for dep_id, dep in self.dependances_externes.items()
            if dep.type_dependance == "critique"
        }
        
        # Analyse par domaine
        analyse_domaines = {}
        for domaine in DomaineSouverainete:
            deps_domaine = [
                dep for dep in dependances_critiques.values()
                if dep.domaine == domaine
            ]
            
            if deps_domaine:
                analyse_domaines[domaine.value] = {
                    "nombre_dependances": len(deps_domaine),
                    "criticite_moyenne": sum(dep.niveau_criticite for dep in deps_domaine) / len(deps_domaine),
                    "risque_cumule": self._calculer_risque_cumule(deps_domaine),
                    "alternatives_disponibles": sum(len(dep.alternatives_disponibles) for dep in deps_domaine),
                    "cout_elimination_total": sum(dep.cout_elimination for dep in deps_domaine)
                }
        
        # Identification des dépendances les plus critiques
        deps_triees = sorted(
            dependances_critiques.values(),
            key=lambda x: x.niveau_criticite * x.risque_rupture,
            reverse=True
        )
        
        return {
            "nombre_dependances_critiques": len(dependances_critiques),
            "analyse_par_domaine": analyse_domaines,
            "dependances_prioritaires": [
                {
                    "nom": dep.nom,
                    "domaine": dep.domaine.value,
                    "criticite": dep.niveau_criticite,
                    "risque": dep.risque_rupture,
                    "alternatives": len(dep.alternatives_disponibles)
                }
                for dep in deps_triees[:5]  # Top 5
            ],
            "impact_souverainete_total": sum(dep.impact_souverainete for dep in dependances_critiques.values()),
            "recommandations_reduction": self._recommander_reduction_dependances(deps_triees)
        }
    
    def planifier_renforcement_souverainete(self, objectif_niveau: float,
                                          horizon: timedelta) -> Dict[str, Any]:
        """
        Planifie le renforcement de la souveraineté vers un niveau objectif.
        
        Args:
            objectif_niveau: Niveau de souveraineté visé (0.0 à 1.0)
            horizon: Horizon temporel pour atteindre l'objectif
            
        Returns:
            Dict: Plan de renforcement détaillé
        """
        niveau_actuel = self._calculer_niveau_global()
        ecart = objectif_niveau - niveau_actuel
        
        if ecart <= 0:
            return {
                "message": "Niveau objectif déjà atteint ou dépassé",
                "niveau_actuel": niveau_actuel,
                "objectif": objectif_niveau
            }
        
        # Identification des domaines à prioriser
        domaines_prioritaires = self._identifier_domaines_prioritaires(objectif_niveau)
        
        # Planification des actions par domaine
        actions_planifiees = {}
        cout_total = 0.0
        impact_prevu = 0.0
        
        for domaine, priorite in domaines_prioritaires.items():
            actions_domaine = self._planifier_actions_domaine(domaine, priorite, horizon)
            actions_planifiees[domaine.value] = actions_domaine
            cout_total += actions_domaine.get("cout_estime", 0.0)
            impact_prevu += actions_domaine.get("impact_souverainete", 0.0)
        
        # Ordonnancement optimal des actions
        sequence_optimale = self._optimiser_sequence_actions(actions_planifiees, horizon)
        
        # Évaluation de la faisabilité
        faisabilite = self._evaluer_faisabilite_plan(cout_total, horizon)
        
        return {
            "objectif_niveau": objectif_niveau,
            "niveau_actuel": niveau_actuel,
            "ecart_a_combler": ecart,
            "horizon_jours": horizon.days,
            "domaines_prioritaires": {
                domaine.value: priorite for domaine, priorite in domaines_prioritaires.items()
            },
            "actions_par_domaine": actions_planifiees,
            "sequence_optimale": sequence_optimale,
            "cout_total_estime": cout_total,
            "impact_souverainete_prevu": impact_prevu,
            "faisabilite": faisabilite,
            "risques_identifies": self._identifier_risques_plan(actions_planifiees),
            "metriques_succes": self._definir_metriques_succes(objectif_niveau)
        }
    
    def detecter_menaces_souverainete(self, signaux_externes: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Détecte les menaces potentielles à la souveraineté.
        
        Args:
            signaux_externes: Signaux provenant de l'environnement externe
            
        Returns:
            Dict: Analyse des menaces détectées
        """
        menaces_detectees = []
        
        for signal in signaux_externes:
            menace = self._analyser_signal_menace(signal)
            if menace and menace["niveau_menace"] > 0.3:
                menaces_detectees.append(menace)
        
        # Classification des menaces par domaine
        menaces_par_domaine = {}
        for domaine in DomaineSouverainete:
            menaces_domaine = [
                m for m in menaces_detectees
                if m.get("domaine_affecte") == domaine.value
            ]
            if menaces_domaine:
                menaces_par_domaine[domaine.value] = menaces_domaine
        
        # Évaluation du niveau de menace global
        niveau_menace_global = self._calculer_niveau_menace_global(menaces_detectees)
        
        # Génération des contre-mesures recommandées
        contre_mesures = self._generer_contre_mesures(menaces_detectees)
        
        return {
            "timestamp": datetime.now(),
            "nombre_menaces": len(menaces_detectees),
            "niveau_menace_global": niveau_menace_global,
            "menaces_par_domaine": menaces_par_domaine,
            "menaces_critiques": [
                m for m in menaces_detectees
                if m["niveau_menace"] > 0.8
            ],
            "contre_mesures_recommandees": contre_mesures,
            "impact_potentiel_souverainete": sum(
                m.get("impact_souverainete", 0.0) for m in menaces_detectees
            ),
            "urgence_reponse": self._evaluer_urgence_reponse(menaces_detectees)
        }
    
    # Méthodes privées pour l'implémentation interne
    
    def _initialiser_metriques_domaines(self):
        """Initialise les métriques pour tous les domaines de souveraineté."""
        for domaine in DomaineSouverainete:
            self.metriques_domaines[domaine] = MetriqueSouverainete(
                domaine=domaine,
                niveau=0.5,  # Niveau initial neutre
                facteurs_contributifs=[],
                dependances_externes=[],
                capacites_internes=[],
                vulnerabilites=[]
            )
    
    def _evaluer_souverainete_domaine(self, domaine: DomaineSouverainete, 
                                    contexte: Dict[str, Any]):
        """Évalue la souveraineté pour un domaine spécifique."""
        metrique = self.metriques_domaines[domaine]
        
        # Analyse des dépendances externes pour ce domaine
        deps_domaine = [
            dep for dep in self.dependances_externes.values()
            if dep.domaine == domaine
        ]
        
        # Analyse des capacités internes pour ce domaine
        caps_domaine = [
            cap for cap in self.capacites_internes.values()
            if cap.domaine == domaine
        ]
        
        # Calcul du niveau de souveraineté
        if deps_domaine:
            impact_dependances = sum(dep.impact_souverainete for dep in deps_domaine) / len(deps_domaine)
        else:
            impact_dependances = 0.0
        
        if caps_domaine:
            contribution_capacites = sum(cap.autonomie_conferee for cap in caps_domaine) / len(caps_domaine)
        else:
            contribution_capacites = 0.5
        
        # Formule de calcul de la souveraineté du domaine
        niveau_domaine = max(0.0, min(1.0, 
            contribution_capacites - (impact_dependances * 0.5) + 
            contexte.get(f"bonus_{domaine.value}", 0.0)
        ))
        
        # Mise à jour de la métrique
        metrique.niveau = niveau_domaine
        metrique.dependances_externes = [dep.nom for dep in deps_domaine]
        metrique.capacites_internes = [cap.nom for cap in caps_domaine]
        metrique.timestamp = datetime.now()
        
        # Identification des vulnérabilités
        metrique.vulnerabilites = self._identifier_vulnerabilites_domaine(domaine, deps_domaine, caps_domaine)
    
    def _calculer_niveau_global(self) -> float:
        """Calcule le niveau global de souveraineté."""
        if not self.metriques_domaines:
            return 0.5
        
        # Pondération des domaines selon leur importance stratégique
        ponderations = {
            DomaineSouverainete.DONNEES: 0.25,
            DomaineSouverainete.ALGORITHMES: 0.20,
            DomaineSouverainete.INFRASTRUCTURE: 0.20,
            DomaineSouverainete.COMMUNICATION: 0.15,
            DomaineSouverainete.DECISION: 0.15,
            DomaineSouverainete.RESSOURCES: 0.05
        }
        
        niveau_pondere = sum(
            metrique.niveau * ponderations.get(domaine, 0.1)
            for domaine, metrique in self.metriques_domaines.items()
        )
        
        return min(1.0, max(0.0, niveau_pondere))
    
    def _determiner_niveau_souverainete(self, niveau_numerique: float) -> NiveauSouverainete:
        """Détermine le niveau de souveraineté à partir d'un score numérique."""
        if niveau_numerique < self.seuils_criticite["assujettissement"]:
            return NiveauSouverainete.ASSUJETTI
        elif niveau_numerique < self.seuils_criticite["dependance"]:
            return NiveauSouverainete.DEPENDANT
        elif niveau_numerique < self.seuils_criticite["autonomie"]:
            return NiveauSouverainete.AUTONOME
        elif niveau_numerique < self.seuils_criticite["souverainete"]:
            return NiveauSouverainete.SOUVERAIN
        else:
            return NiveauSouverainete.HEGEMONE
    
    def _identifier_vulnerabilites_souverainete(self) -> List[Dict[str, Any]]:
        """Identifie les vulnérabilités majeures de la souveraineté."""
        vulnerabilites = []
        
        for domaine, metrique in self.metriques_domaines.items():
            if metrique.niveau < 0.4:  # Seuil de vulnérabilité
                vulnerabilites.append({
                    "domaine": domaine.value,
                    "niveau_souverainete": metrique.niveau,
                    "vulnerabilites_specifiques": metrique.vulnerabilites,
                    "criticite": 1.0 - metrique.niveau,
                    "impact_potentiel": self._estimer_impact_vulnerabilite(domaine)
                })
        
        return sorted(vulnerabilites, key=lambda x: x["criticite"], reverse=True)
    
    def _identifier_opportunites_souverainete(self) -> List[Dict[str, Any]]:
        """Identifie les opportunités de renforcement de la souveraineté."""
        opportunites = []
        
        # Opportunités d'amélioration des capacités internes
        for cap_id, capacite in self.capacites_internes.items():
            if capacite.potentiel_evolution > 0.3:
                opportunites.append({
                    "type": "amelioration_capacite",
                    "cible": capacite.nom,
                    "domaine": capacite.domaine.value,
                    "potentiel": capacite.potentiel_evolution,
                    "cout_estime": capacite.cout_maintenance * 2,
                    "impact_souverainete": capacite.potentiel_evolution * 0.7
                })
        
        # Opportunités de réduction des dépendances
        for dep_id, dependance in self.dependances_externes.items():
            if dependance.alternatives_disponibles:
                opportunites.append({
                    "type": "reduction_dependance",
                    "cible": dependance.nom,
                    "domaine": dependance.domaine.value,
                    "potentiel": dependance.impact_souverainete,
                    "cout_estime": dependance.cout_elimination,
                    "impact_souverainete": dependance.impact_souverainete
                })
        
        return sorted(opportunites, key=lambda x: x["impact_souverainete"], reverse=True)
    
    def _generer_strategie_souverainete(self, vulnerabilites: List[Dict], 
                                      opportunites: List[Dict],
                                      contexte: Dict[str, Any]) -> Dict[str, Any]:
        """Génère une stratégie de renforcement de la souveraineté."""
        # Priorisation basée sur le contexte polyvagal
        etat_polyvagal = contexte.get("etat_polyvagal", "VENTRAL")
        
        if etat_polyvagal == "DORSAL":
            # En mode défensif, focus sur la protection
            strategie = {
                "approche": "defensive",
                "priorite": "protection_acquis",
                "actions_immediates": [
                    "renforcement_capacites_critiques",
                    "reduction_dependances_risquees",
                    "isolation_protective"
                ],
                "horizon": "court_terme"
            }
        elif etat_polyvagal == "SYMPATHETIC":
            # En mode adaptatif, focus sur l'optimisation
            strategie = {
                "approche": "adaptative",
                "priorite": "optimisation_equilibre",
                "actions_immediates": [
                    "diversification_capacites",
                    "negociation_dependances",
                    "exploration_alternatives"
                ],
                "horizon": "moyen_terme"
            }
        else:  # VENTRAL
            # En mode créatif, focus sur l'expansion
            strategie = {
                "approche": "expansive",
                "priorite": "innovation_souverainete",
                "actions_immediates": [
                    "developpement_nouvelles_capacites",
                    "creation_ecosysteme_autonome",
                    "leadership_souverainete"
                ],
                "horizon": "long_terme"
            }
        
        # Ajout des actions spécifiques basées sur l'analyse
        strategie["actions_vulnerabilites"] = [
            {
                "domaine": vuln["domaine"],
                "action": f"renforcer_{vuln['domaine']}",
                "priorite": vuln["criticite"]
            }
            for vuln in vulnerabilites[:3]  # Top 3 vulnérabilités
        ]
        
        strategie["actions_opportunites"] = [
            {
                "type": opp["type"],
                "cible": opp["cible"],
                "impact_prevu": opp["impact_souverainete"]
            }
            for opp in opportunites[:5]  # Top 5 opportunités
        ]
        
        return strategie
    
    def _calculer_indice_resilience(self) -> float:
        """Calcule l'indice de résilience de la souveraineté."""
        # Combinaison de plusieurs facteurs
        diversification = self._calculer_diversification_capacites()
        robustesse = self._calculer_robustesse_dependances()
        adaptabilite = self._calculer_adaptabilite_souverainete()
        
        return (diversification + robustesse + adaptabilite) / 3
    
    def _maintenir_historique(self):
        """Maintient l'historique en supprimant les anciennes entrées."""
        if len(self.historique_souverainete) > 1000:
            self.historique_souverainete = self.historique_souverainete[-500:]
    
    # Méthodes utilitaires supplémentaires
    
    def _calculer_risque_cumule(self, dependances: List[DependanceExterne]) -> float:
        """Calcule le risque cumulé d'un ensemble de dépendances."""
        if not dependances:
            return 0.0
        
        # Calcul du risque comme probabilité composée
        risque_cumule = 1.0
        for dep in dependances:
            risque_cumule *= (1.0 - dep.risque_rupture)
        
        return 1.0 - risque_cumule
    
    def _recommander_reduction_dependances(self, dependances: List[DependanceExterne]) -> List[str]:
        """Recommande des actions pour réduire les dépendances."""
        recommandations = []
        
        for dep in dependances[:3]:  # Top 3
            if dep.alternatives_disponibles:
                recommandations.append(f"Migrer vers alternative pour {dep.nom}")
            else:
                recommandations.append(f"Développer alternative interne pour {dep.nom}")
            
            if dep.type_dependance == "critique":
                recommandations.append(f"Créer redondance pour {dep.nom}")
        
        return recommandations
    
    def _identifier_domaines_prioritaires(self, objectif: float) -> Dict[DomaineSouverainete, float]:
        """Identifie les domaines prioritaires pour atteindre l'objectif."""
        priorites = {}
        
        for domaine, metrique in self.metriques_domaines.items():
            ecart = objectif - metrique.niveau
            if ecart > 0:
                priorites[domaine] = ecart
        
        return dict(sorted(priorites.items(), key=lambda x: x[1], reverse=True))
    
    def _planifier_actions_domaine(self, domaine: DomaineSouverainete, 
                                 priorite: float, horizon: timedelta) -> Dict[str, Any]:
        """Planifie les actions pour un domaine spécifique."""
        return {
            "actions": [f"action_placeholder_{domaine.value}"],
            "cout_estime": priorite * 1000,
            "impact_souverainete": priorite * 0.8,
            "duree_prevue_jours": horizon.days * priorite
        }
    
    def _optimiser_sequence_actions(self, actions: Dict, horizon: timedelta) -> List[Dict]:
        """Optimise la séquence d'exécution des actions."""
        return [{"sequence": "optimisation_placeholder"}]
    
    def _evaluer_faisabilite_plan(self, cout_total: float, horizon: timedelta) -> Dict[str, Any]:
        """Évalue la faisabilité du plan."""
        return {
            "faisable": cout_total < 10000,  # Seuil arbitraire
            "contraintes": ["ressources", "temps"],
            "recommandations": ["echelonner_actions"]
        }
    
    def _identifier_risques_plan(self, actions: Dict) -> List[str]:
        """Identifie les risques du plan."""
        return ["risque_placeholder"]
    
    def _definir_metriques_succes(self, objectif: float) -> Dict[str, float]:
        """Définit les métriques de succès."""
        return {
            "niveau_souverainete_cible": objectif,
            "seuil_minimal_acceptable": objectif * 0.9
        }
    
    def _analyser_signal_menace(self, signal: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Analyse un signal pour détecter une menace potentielle."""
        # Analyse simplifiée - dans un vrai système, utiliser des heuristiques sophistiquées
        if signal.get("type") == "intrusion" or signal.get("anomalie", False):
            return {
                "type_menace": signal.get("type", "inconnue"),
                "niveau_menace": signal.get("severite", 0.5),
                "domaine_affecte": "infrastructure",  # Exemple
                "impact_souverainete": signal.get("impact", 0.3),
                "actions_recommandees": ["surveillance_renforcee"]
            }
        return None
    
    def _calculer_niveau_menace_global(self, menaces: List[Dict]) -> float:
        """Calcule le niveau de menace global."""
        if not menaces:
            return 0.0
        
        niveaux = [m["niveau_menace"] for m in menaces]
        return max(niveaux)
    
    def _generer_contre_mesures(self, menaces: List[Dict]) -> List[str]:
        """Génère des contre-mesures pour les menaces détectées."""
        contre_mesures = []
        
        for menace in menaces:
            if menace["niveau_menace"] > 0.7:
                contre_mesures.append(f"Activer protocole urgence pour {menace['type_menace']}")
            else:
                contre_mesures.append(f"Surveiller évolution {menace['type_menace']}")
        
        return contre_mesures
    
    def _evaluer_urgence_reponse(self, menaces: List[Dict]) -> str:
        """Évalue l'urgence de la réponse nécessaire."""
        if any(m["niveau_menace"] > 0.9 for m in menaces):
            return "immediate"
        elif any(m["niveau_menace"] > 0.7 for m in menaces):
            return "rapide"
        elif any(m["niveau_menace"] > 0.5 for m in menaces):
            return "moderee"
        else:
            return "faible"
    
    def _identifier_vulnerabilites_domaine(self, domaine: DomaineSouverainete,
                                         dependances: List[DependanceExterne],
                                         capacites: List[CapaciteInterne]) -> List[str]:
        """Identifie les vulnérabilités spécifiques d'un domaine."""
        vulnerabilites = []
        
        # Vulnérabilités liées aux dépendances
        for dep in dependances:
            if dep.niveau_criticite > 0.7 and not dep.alternatives_disponibles:
                vulnerabilites.append(f"Dépendance critique sans alternative: {dep.nom}")
        
        # Vulnérabilités liées aux capacités
        capacites_faibles = [cap for cap in capacites if cap.niveau_maturite < 0.5]
        if len(capacites_faibles) > len(capacites) * 0.5:
            vulnerabilites.append("Capacités internes insuffisamment développées")
        
        return vulnerabilites
    
    def _estimer_impact_vulnerabilite(self, domaine: DomaineSouverainete) -> float:
        """Estime l'impact potentiel d'une vulnérabilité."""
        # Impact différencié selon le domaine
        impacts = {
            DomaineSouverainete.DONNEES: 0.9,
            DomaineSouverainete.ALGORITHMES: 0.8,
            DomaineSouverainete.INFRASTRUCTURE: 0.85,
            DomaineSouverainete.COMMUNICATION: 0.7,
            DomaineSouverainete.DECISION: 0.95,
            DomaineSouverainete.RESSOURCES: 0.6
        }
        return impacts.get(domaine, 0.7)
    
    def _calculer_diversification_capacites(self) -> float:
        """Calcule l'indice de diversification des capacités."""
        if not self.capacites_internes:
            return 0.0
        
        # Diversification basée sur la répartition entre domaines
        domaines_couverts = set(cap.domaine for cap in self.capacites_internes.values())
        return len(domaines_couverts) / len(DomaineSouverainete)
    
    def _calculer_robustesse_dependances(self) -> float:
        """Calcule l'indice de robustesse face aux dépendances."""
        if not self.dependances_externes:
            return 1.0
        
        # Robustesse inversement proportionnelle aux dépendances critiques
        deps_critiques = [
            dep for dep in self.dependances_externes.values()
            if dep.type_dependance == "critique"
        ]
        
        ratio_critiques = len(deps_critiques) / len(self.dependances_externes)
        return max(0.0, 1.0 - ratio_critiques)
    
    def _calculer_adaptabilite_souverainete(self) -> float:
        """Calcule l'indice d'adaptabilité de la souveraineté."""
        # Basé sur la capacité d'évolution des capacités internes
        if not self.capacites_internes:
            return 0.5
        
        potentiels = [cap.potentiel_evolution for cap in self.capacites_internes.values()]
        return sum(potentiels) / len(potentiels)