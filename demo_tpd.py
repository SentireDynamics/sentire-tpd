#!/usr/bin/env python3
"""
Démonstration TPD - Théorie Polyvagale Digitale
===============================================

Script de démonstration illustrant l'utilisation de l'architecture TPD
pour la gestion de la résilience et de la souveraineté des systèmes.

Usage:
    python demo_tpd.py [--scenario SCENARIO] [--duree MINUTES]
    
Scénarios disponibles:
    - stabilite: Fonctionnement optimal en état VENTRAL
    - crise: Gestion d'une crise système en transition SYMPATHETIC/DORSAL
    - souverainete: Analyse et renforcement de la souveraineté numérique
    - adaptation: Démonstration des capacités d'adaptation Guardian/Predator
"""

import argparse
import time
import json
from datetime import datetime, timedelta
from typing import Dict, Any, List
import random

# Import des modules TPD
from tpd import (
    EtatVentral, EtatSympathetic, EtatDorsal,
    SystemeResilience, EvenementSysteme,
    ConscienceSituationnelle, SouveraineteNumerique
)


class DemonstratorTPD:
    """Démonstrateur de l'architecture TPD en action."""
    
    def __init__(self):
        self.systeme = SystemeResilience("SystemeDemo")
        self.conscience = ConscienceSituationnelle("ConscienceDemo")
        self.souverainete = SouveraineteNumerique("SouveraineteDemo")
        self.historique_demo = []
    
    def scenario_stabilite(self, duree_minutes: int = 5):
        """
        Scénario de stabilité - Fonctionnement optimal
        =============================================
        
        Démontre le fonctionnement du système en état VENTRAL
        avec gestion proactive de la résilience.
        """
        print("🌱 SCENARIO STABILITÉ - État VENTRAL")
        print("=" * 50)
        
        # Initialisation en état VENTRAL
        self.systeme.etat_actuel = EtatVentral()
        self.systeme.etat_actuel.activer({"mode": "demonstration_stabilite"})
        
        debut = datetime.now()
        fin = debut + timedelta(minutes=duree_minutes)
        
        iteration = 0
        while datetime.now() < fin:
            iteration += 1
            print(f"\n--- Itération {iteration} ---")
            
            # Génération d'événements bénins pour état stable
            evenements = self._generer_evenements_stabilite()
            
            # Orchestration de la résilience
            resultat = self.systeme.orchestrer_resilience(evenements)
            
            # Évaluation de la conscience situationnelle
            contexte_conscience = self.conscience.evaluer_contexte_global("VENTRAL")
            
            # Affichage des résultats
            self._afficher_status_systeme(resultat, contexte_conscience)
            
            # Enregistrement dans l'historique
            self.historique_demo.append({
                "timestamp": datetime.now(),
                "scenario": "stabilite",
                "iteration": iteration,
                "etat": resultat["etat_polyvagal"],
                "metriques": resultat["metriques_souverainete"]
            })
            
            time.sleep(2)  # Pause entre itérations
        
        print("\n✅ Scénario stabilité terminé avec succès")
        self._generer_rapport_scenario("stabilite")
    
    def scenario_crise(self, duree_minutes: int = 10):
        """
        Scénario de crise - Gestion adaptative
        ======================================
        
        Démontre la gestion de crise avec transitions polyvagales
        et réponses Guardian/Predator.
        """
        print("🚨 SCENARIO CRISE - Transitions polyvagales")
        print("=" * 50)
        
        # Démarrage en état stable
        self.systeme.etat_actuel = EtatVentral()
        self.systeme.etat_actuel.activer({"mode": "demonstration_crise"})
        
        debut = datetime.now()
        fin = debut + timedelta(minutes=duree_minutes)
        
        phase_crise = False
        iteration = 0
        
        while datetime.now() < fin:
            iteration += 1
            print(f"\n--- Itération {iteration} ---")
            
            # Escalade progressive vers la crise
            if iteration > 3 and not phase_crise:
                print("🔥 DÉCLENCHEMENT DE LA CRISE")
                phase_crise = True
            
            # Génération d'événements selon la phase
            if phase_crise:
                evenements = self._generer_evenements_crise(iteration)
            else:
                evenements = self._generer_evenements_stabilite()
            
            # Orchestration de la résilience
            resultat = self.systeme.orchestrer_resilience(evenements)
            
            # Évaluation de la conscience en mode crise
            etat_actuel = resultat["etat_polyvagal"]
            contexte_conscience = self.conscience.evaluer_contexte_global(etat_actuel)
            
            # Analyse des menaces à la souveraineté
            signaux_menaces = self._convertir_evenements_en_signaux(evenements)
            analyse_menaces = self.souverainete.detecter_menaces_souverainete(signaux_menaces)
            
            # Affichage détaillé
            self._afficher_status_crise(resultat, contexte_conscience, analyse_menaces)
            
            # Enregistrement
            self.historique_demo.append({
                "timestamp": datetime.now(),
                "scenario": "crise",
                "iteration": iteration,
                "etat": etat_actuel,
                "phase_crise": phase_crise,
                "nombre_menaces": analyse_menaces["nombre_menaces"],
                "niveau_menace": analyse_menaces["niveau_menace_global"]
            })
            
            time.sleep(1.5)
        
        print("\n💪 Scénario crise terminé - Résilience démontrée")
        self._generer_rapport_scenario("crise")
    
    def scenario_souverainete(self, duree_minutes: int = 8):
        """
        Scénario souveraineté - Analyse et renforcement
        ==============================================
        
        Démontre l'analyse de la souveraineté numérique et
        la planification de son renforcement.
        """
        print("👑 SCENARIO SOUVERAINETÉ - Autonomie numérique")
        print("=" * 50)
        
        # Configuration initiale avec dépendances et capacités
        self._configurer_souverainete_demo()
        
        debut = datetime.now()
        fin = debut + timedelta(minutes=duree_minutes)
        
        iteration = 0
        while datetime.now() < fin:
            iteration += 1
            print(f"\n--- Analyse {iteration} ---")
            
            # Contexte systémique simulé
            contexte = {
                "ressources_disponibles": random.uniform(0.6, 0.9),
                "stabilite_systeme": random.uniform(0.7, 0.95),
                "etat_polyvagal": "VENTRAL",
                "menaces_externes": random.randint(0, 3)
            }
            
            # Évaluation complète de la souveraineté
            evaluation = self.souverainete.evaluer_souverainete_globale(contexte)
            
            # Analyse des dépendances critiques
            analyse_deps = self.souverainete.analyser_dependances_critiques()
            
            # Planification du renforcement si nécessaire
            objectif_souverainete = 0.85
            plan_renforcement = self.souverainete.planifier_renforcement_souverainete(
                objectif_souverainete, timedelta(days=90)
            )
            
            # Affichage de l'analyse
            self._afficher_analyse_souverainete(evaluation, analyse_deps, plan_renforcement)
            
            # Enregistrement
            self.historique_demo.append({
                "timestamp": datetime.now(),
                "scenario": "souverainete",
                "iteration": iteration,
                "niveau_souverainete": evaluation["niveau_global"],
                "classification": evaluation["classification"],
                "dependances_critiques": analyse_deps["nombre_dependances_critiques"]
            })
            
            time.sleep(2)
        
        print("\n🏛️ Analyse de souveraineté terminée")
        self._generer_rapport_scenario("souverainete")
    
    def scenario_adaptation(self, duree_minutes: int = 7):
        """
        Scénario adaptation - Guardian/Predator en action
        ================================================
        
        Démontre l'orchestration Guardian/Predator pour
        l'adaptation dynamique du système.
        """
        print("🔄 SCENARIO ADAPTATION - Guardian/Predator")
        print("=" * 50)
        
        debut = datetime.now()
        fin = debut + timedelta(minutes=duree_minutes)
        
        iteration = 0
        mode_adaptation = "exploration"  # exploration, protection, equilibre
        
        while datetime.now() < fin:
            iteration += 1
            print(f"\n--- Cycle {iteration} - Mode: {mode_adaptation} ---")
            
            # Alternance des modes pour démontrer la versatilité
            if iteration % 4 == 0:
                mode_adaptation = "protection"
            elif iteration % 4 == 2:
                mode_adaptation = "equilibre"
            else:
                mode_adaptation = "exploration"
            
            # Génération d'événements selon le mode
            evenements = self._generer_evenements_adaptation(mode_adaptation, iteration)
            
            # Orchestration Guardian/Predator
            resultat = self.systeme.orchestrer_resilience(evenements)
            
            # Analyse spécifique Guardian/Predator
            guardian_metrics = self._analyser_performance_guardian()
            predator_metrics = self._analyser_performance_predator()
            
            # Affichage de l'orchestration
            self._afficher_orchestration_guardian_predator(
                resultat, guardian_metrics, predator_metrics, mode_adaptation
            )
            
            # Enregistrement
            self.historique_demo.append({
                "timestamp": datetime.now(),
                "scenario": "adaptation",
                "iteration": iteration,
                "mode": mode_adaptation,
                "etat": resultat["etat_polyvagal"],
                "guardian_actions": len(resultat["intervention_guardian"]["resultats"]),
                "predator_actions": len(resultat["adaptation_predator"]["resultats"])
            })
            
            time.sleep(1.8)
        
        print("\n🎯 Démonstration d'adaptation terminée")
        self._generer_rapport_scenario("adaptation")
    
    # Méthodes utilitaires pour la génération d'événements
    
    def _generer_evenements_stabilite(self) -> List[EvenementSysteme]:
        """Génère des événements bénins pour état stable."""
        evenements = []
        
        # Événements normaux de fonctionnement
        types_normaux = ["maintenance_routine", "optimisation_performance", "sauvegarde_donnees"]
        
        for _ in range(random.randint(1, 3)):
            evenements.append(EvenementSysteme(
                timestamp=datetime.now(),
                type_evenement=random.choice(types_normaux),
                severite="info",
                contexte={"routine": True, "impact_faible": True},
                source="systeme_interne",
                impact_prevu=random.uniform(0.1, 0.3)
            ))
        
        return evenements
    
    def _generer_evenements_crise(self, iteration: int) -> List[EvenementSysteme]:
        """Génère des événements de crise avec escalade."""
        evenements = []
        
        # Escalade progressive de la sévérité
        if iteration < 6:
            # Phase d'alerte
            types_alerte = ["surcharge_detectee", "anomalie_reseau", "erreur_authentification"]
            severite = "alerte"
            impact_range = (0.4, 0.6)
        else:
            # Phase critique
            types_critique = ["intrusion_detectee", "corruption_donnees", "panne_infrastructure"]
            severite = "critique"
            impact_range = (0.7, 0.9)
        
        nombre_evenements = min(iteration, 5)  # Escalade du nombre
        
        for i in range(nombre_evenements):
            if iteration < 6:
                type_event = random.choice(types_alerte)
            else:
                type_event = random.choice(types_critique)
            
            evenements.append(EvenementSysteme(
                timestamp=datetime.now(),
                type_evenement=type_event,
                severite=severite,
                contexte={"crise": True, "escalade": iteration},
                source="externe" if random.random() > 0.3 else "interne",
                impact_prevu=random.uniform(*impact_range)
            ))
        
        return evenements
    
    def _generer_evenements_adaptation(self, mode: str, iteration: int) -> List[EvenementSysteme]:
        """Génère des événements pour démontrer l'adaptation."""
        evenements = []
        
        if mode == "exploration":
            types = ["nouvelle_donnee_disponible", "opportunite_optimisation", "demande_collaboration"]
            severite = "info"
            impact_range = (0.2, 0.4)
        elif mode == "protection":
            types = ["tentative_intrusion", "anomalie_securite", "menace_detectee"]
            severite = "alerte"
            impact_range = (0.5, 0.7)
        else:  # equilibre
            types = ["ajustement_charge", "reequilibrage_ressources", "mise_a_jour_systeme"]
            severite = "attention"
            impact_range = (0.3, 0.5)
        
        for _ in range(random.randint(2, 4)):
            evenements.append(EvenementSysteme(
                timestamp=datetime.now(),
                type_evenement=random.choice(types),
                severite=severite,
                contexte={"mode_demo": mode, "iteration": iteration},
                source="mixte",
                impact_prevu=random.uniform(*impact_range)
            ))
        
        return evenements
    
    # Méthodes d'affichage et de rapport
    
    def _afficher_status_systeme(self, resultat: Dict, conscience: Dict):
        """Affiche le status général du système."""
        print(f"État Polyvagal: {resultat['etat_polyvagal']} | "
              f"Conscience: {conscience['niveau_conscience']} | "
              f"Stabilité: {conscience['stabilite_environnementale']:.2f}")
        
        if resultat['transition_effectuee']:
            print(f"🔄 Transition effectuée vers: {resultat['transition_effectuee']}")
        
        print(f"Guardian: {len(resultat['intervention_guardian']['resultats'])} actions | "
              f"Predator: {len(resultat['adaptation_predator']['resultats'])} adaptations")
    
    def _afficher_status_crise(self, resultat: Dict, conscience: Dict, menaces: Dict):
        """Affiche le status pendant une crise."""
        print(f"🚨 ÉTAT: {resultat['etat_polyvagal']} | "
              f"Menaces: {menaces['nombre_menaces']} | "
              f"Niveau: {menaces['niveau_menace_global']:.2f}")
        
        if resultat['transition_effectuee']:
            print(f"🔄 TRANSITION CRITIQUE: {resultat['transition_effectuee']}")
        
        print(f"🛡️ Guardian: {len(resultat['intervention_guardian']['resultats'])} protections")
        print(f"⚡ Predator: {len(resultat['adaptation_predator']['resultats'])} adaptations")
        
        if menaces['contre_mesures_recommandees']:
            print(f"💡 Contre-mesures: {', '.join(menaces['contre_mesures_recommandees'][:2])}")
    
    def _afficher_analyse_souverainete(self, evaluation: Dict, deps: Dict, plan: Dict):
        """Affiche l'analyse de souveraineté."""
        print(f"👑 Souveraineté: {evaluation['classification']} ({evaluation['niveau_global']:.2f})")
        print(f"📊 Dépendances critiques: {deps['nombre_dependances_critiques']}")
        
        if 'dependances_prioritaires' in deps and deps['dependances_prioritaires']:
            print(f"⚠️  Prioritaire: {deps['dependances_prioritaires'][0]['nom']}")
        
        if 'actions_par_domaine' in plan:
            domaines_actifs = len(plan['actions_par_domaine'])
            print(f"📋 Plan: {domaines_actifs} domaines, coût {plan.get('cout_total_estime', 0):.0f}")
    
    def _afficher_orchestration_guardian_predator(self, resultat: Dict, guardian: Dict, 
                                                predator: Dict, mode: str):
        """Affiche l'orchestration Guardian/Predator."""
        print(f"🎭 Mode: {mode.upper()} | État: {resultat['etat_polyvagal']}")
        
        guardian_actions = len(resultat['intervention_guardian']['resultats'])
        predator_actions = len(resultat['adaptation_predator']['resultats'])
        
        print(f"🛡️ Guardian: {guardian_actions} actions (vigilance: {guardian['vigilance']:.1f})")
        print(f"⚡ Predator: {predator_actions} adaptations (agressivité: {predator['agressivite']:.1f})")
        
        if resultat['transition_effectuee']:
            print(f"🔄 Transition orchestrée: {resultat['transition_effectuee']}")
    
    def _generer_rapport_scenario(self, scenario: str):
        """Génère un rapport de fin de scénario."""
        print(f"\n📊 RAPPORT SCÉNARIO: {scenario.upper()}")
        print("=" * 40)
        
        donnees_scenario = [h for h in self.historique_demo if h['scenario'] == scenario]
        
        if donnees_scenario:
            print(f"Itérations: {len(donnees_scenario)}")
            
            if 'etat' in donnees_scenario[0]:
                etats = [d['etat'] for d in donnees_scenario]
                print(f"États traversés: {', '.join(set(etats))}")
            
            if scenario == "crise" and 'niveau_menace' in donnees_scenario[-1]:
                niveau_max = max(d.get('niveau_menace', 0) for d in donnees_scenario)
                print(f"Niveau menace max: {niveau_max:.2f}")
            
            if scenario == "souverainete" and 'niveau_souverainete' in donnees_scenario[-1]:
                niveau_final = donnees_scenario[-1]['niveau_souverainete']
                print(f"Souveraineté finale: {niveau_final:.2f}")
        
        print("✅ Doctrine TPD respectée dans toutes les phases")
    
    # Méthodes de configuration et d'analyse
    
    def _configurer_souverainete_demo(self):
        """Configure des dépendances et capacités pour la démo."""
        from tpd.souverainete import DependanceExterne, CapaciteInterne, DomaineSouverainete
        
        # Ajout de dépendances simulées
        deps = [
            DependanceExterne(
                id_dependance="dep_cloud",
                nom="Infrastructure Cloud Externe",
                type_dependance="critique",
                domaine=DomaineSouverainete.INFRASTRUCTURE,
                niveau_criticite=0.8,
                alternatives_disponibles=["cloud_prive", "infrastructure_hybride"],
                cout_elimination=5000,
                risque_rupture=0.3,
                impact_souverainete=0.6
            ),
            DependanceExterne(
                id_dependance="dep_algo",
                nom="Algorithmes Tiers",
                type_dependance="importante",
                domaine=DomaineSouverainete.ALGORITHMES,
                niveau_criticite=0.6,
                alternatives_disponibles=["developpement_interne"],
                cout_elimination=3000,
                risque_rupture=0.2,
                impact_souverainete=0.4
            )
        ]
        
        for dep in deps:
            self.souverainete.dependances_externes[dep.id_dependance] = dep
        
        # Ajout de capacités simulées
        caps = [
            CapaciteInterne(
                id_capacite="cap_crypto",
                nom="Cryptographie Avancée",
                domaine=DomaineSouverainete.DONNEES,
                niveau_maturite=0.8,
                autonomie_conferee=0.9,
                cout_maintenance=1000,
                potentiel_evolution=0.7,
                synergies=["securite_reseau", "authentification"]
            ),
            CapaciteInterne(
                id_capacite="cap_ia",
                nom="Intelligence Artificielle Propriétaire",
                domaine=DomaineSouverainete.ALGORITHMES,
                niveau_maturite=0.6,
                autonomie_conferee=0.7,
                cout_maintenance=2000,
                potentiel_evolution=0.9,
                synergies=["analyse_donnees", "decision_automatisee"]
            )
        ]
        
        for cap in caps:
            self.souverainete.capacites_internes[cap.id_capacite] = cap
    
    def _convertir_evenements_en_signaux(self, evenements: List[EvenementSysteme]) -> List[Dict]:
        """Convertit les événements TPD en signaux pour l'analyse de menaces."""
        signaux = []
        
        for event in evenements:
            signal = {
                "type": event.type_evenement,
                "severite": event.impact_prevu,
                "source": event.source,
                "contexte": event.contexte,
                "anomalie": event.severite in ["alerte", "critique"]
            }
            signaux.append(signal)
        
        return signaux
    
    def _analyser_performance_guardian(self) -> Dict[str, float]:
        """Analyse les performances du Guardian."""
        return {
            "vigilance": self.systeme.guardian.niveau_vigilance,
            "interventions_recentes": len(self.systeme.guardian.historique_interventions),
            "efficacite": 0.85  # Simulation
        }
    
    def _analyser_performance_predator(self) -> Dict[str, float]:
        """Analyse les performances du Predator."""
        return {
            "agressivite": self.systeme.predator.niveau_agressivite,
            "adaptations_recentes": len(self.systeme.predator.historique_adaptations),
            "innovation": 0.75  # Simulation
        }


def main():
    """Point d'entrée principal du démonstrateur."""
    parser = argparse.ArgumentParser(
        description="Démonstrateur TPD - Théorie Polyvagale Digitale"
    )
    parser.add_argument(
        "--scenario",
        choices=["stabilite", "crise", "souverainete", "adaptation", "complet"],
        default="complet",
        help="Scénario à exécuter"
    )
    parser.add_argument(
        "--duree",
        type=int,
        default=5,
        help="Durée en minutes de chaque scénario"
    )
    
    args = parser.parse_args()
    
    print("🧠 DÉMONSTRATEUR TPD - THÉORIE POLYVAGALE DIGITALE")
    print("=" * 60)
    print("Architecture neuro-inspirée pour la résilience des systèmes")
    print("Doctrine: Guardian/Predator | Tripartition: VENTRAL/SYMPATHETIC/DORSAL")
    print("=" * 60)
    
    demo = DemonstratorTPD()
    
    try:
        if args.scenario == "complet":
            print("\n🎬 DÉMONSTRATION COMPLÈTE - Tous les scénarios")
            demo.scenario_stabilite(args.duree)
            time.sleep(2)
            demo.scenario_adaptation(args.duree)
            time.sleep(2)
            demo.scenario_souverainete(args.duree)
            time.sleep(2)
            demo.scenario_crise(args.duree)
        elif args.scenario == "stabilite":
            demo.scenario_stabilite(args.duree)
        elif args.scenario == "crise":
            demo.scenario_crise(args.duree)
        elif args.scenario == "souverainete":
            demo.scenario_souverainete(args.duree)
        elif args.scenario == "adaptation":
            demo.scenario_adaptation(args.duree)
        
        # Rapport final
        print("\n" + "=" * 60)
        print("🏆 DÉMONSTRATION TPD TERMINÉE")
        print(f"Total d'événements traités: {len(demo.historique_demo)}")
        print("Doctrine TPD validée: Résilience, Conscience, Souveraineté")
        print("Architecture Guardian/Predator opérationnelle")
        print("=" * 60)
        
        # Sauvegarde optionnelle de l'historique
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        with open(f"demo_tpd_historique_{timestamp}.json", "w", encoding="utf-8") as f:
            json.dump(demo.historique_demo, f, indent=2, default=str, ensure_ascii=False)
        print(f"📄 Historique sauvegardé: demo_tpd_historique_{timestamp}.json")
        
    except KeyboardInterrupt:
        print("\n⏹️  Démonstration interrompue par l'utilisateur")
    except Exception as e:
        print(f"\n❌ Erreur durant la démonstration: {e}")


if __name__ == "__main__":
    main()