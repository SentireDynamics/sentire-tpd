#!/usr/bin/env python3
"""
Tests de Validation TPD - Théorie Polyvagale Digitale
=====================================================

Tests unitaires pour valider le bon fonctionnement de l'architecture TPD
selon les principes doctrinaux de résilience et de souveraineté.
"""

import unittest
import sys
import os
from datetime import datetime, timedelta

# Ajout du chemin parent pour l'import des modules TPD
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tpd import (
    EtatVentral, EtatSympathetic, EtatDorsal,
    SystemeResilience, EvenementSysteme,
    ConscienceSituationnelle, SouveraineteNumerique
)
from tpd.etats import NiveauResilience
from tpd.souverainete import DomaineSouverainete, NiveauSouverainete


class TestEtatsPolyvagaux(unittest.TestCase):
    """Tests pour les états polyvagaux fondamentaux."""
    
    def setUp(self):
        """Configuration des tests."""
        self.contexte_test = {
            "ressources_disponibles": 0.8,
            "stabilite_systeme": 0.9,
            "niveau_menace": 0.2,
            "charge_systeme": 0.5
        }
    
    def test_etat_ventral_securite(self):
        """Test de l'état VENTRAL - sécurité et engagement."""
        ventral = EtatVentral()
        
        # Vérification des caractéristiques VENTRAL
        self.assertEqual(ventral.nom, "VENTRAL")
        self.assertEqual(ventral.niveau_resilience, NiveauResilience.SOUVERAIN)
        self.assertIn("SYMPATHETIC", ventral.transitions_permises)
        self.assertIn("DORSAL", ventral.transitions_permises)
        
        # Test de la conscience situationnelle maximale
        conscience = ventral.evaluer_conscience_situationnelle(self.contexte_test)
        self.assertGreaterEqual(conscience, 0.8)  # Conscience élevée en VENTRAL
        
        # Test de la stratégie proactive
        strategie = ventral.calculer_strategie_resilience([])
        self.assertEqual(strategie["approche"], "proactive")
        self.assertEqual(strategie["priorite"], "innovation_preventive")
    
    def test_etat_sympathetic_mobilisation(self):
        """Test de l'état SYMPATHETIC - mobilisation et activation."""
        sympathetic = EtatSympathetic()
        
        # Vérification des caractéristiques SYMPATHETIC
        self.assertEqual(sympathetic.nom, "SYMPATHETIC") 
        self.assertEqual(sympathetic.niveau_resilience, NiveauResilience.ADAPTATIF)
        
        # Test de la conscience focalisée
        contexte_menace = self.contexte_test.copy()
        contexte_menace["detection_anomalies"] = 0.8
        conscience = sympathetic.evaluer_conscience_situationnelle(contexte_menace)
        self.assertLessEqual(conscience, 0.8)  # Plafonnée en SYMPATHETIC
        
        # Test de la stratégie réactive
        perturbations = [{"type": "anomalie", "severite": 0.6}]
        strategie = sympathetic.calculer_strategie_resilience(perturbations)
        self.assertEqual(strategie["approche"], "reactive")
        self.assertEqual(strategie["priorite"], "performance_immediate")
    
    def test_etat_dorsal_conservation(self):
        """Test de l'état DORSAL - conservation et protection."""
        dorsal = EtatDorsal()
        
        # Vérification des caractéristiques DORSAL
        self.assertEqual(dorsal.nom, "DORSAL")
        self.assertEqual(dorsal.niveau_resilience, NiveauResilience.CRITIQUE)
        
        # Test de la conscience minimale
        conscience = dorsal.evaluer_conscience_situationnelle(self.contexte_test)
        self.assertGreaterEqual(conscience, 0.1)  # Minimum vital
        
        # Test de la stratégie défensive
        strategie = dorsal.calculer_strategie_resilience([])
        self.assertEqual(strategie["approche"], "defensive")
        self.assertEqual(strategie["priorite"], "conservation_critique")
        self.assertEqual(strategie["ressources_allouees"], dorsal.ratio_conservation)
    
    def test_transitions_polyvagales(self):
        """Test des transitions entre états polyvagaux."""
        ventral = EtatVentral()
        
        # Transition vers SYMPATHETIC si menace détectée
        contexte_menace = {
            "niveau_menace": 0.9,  # Au-dessus du seuil
            "charge_systeme": 0.5
        }
        transition = ventral.determiner_transition_necessaire(contexte_menace)
        self.assertEqual(transition, "SYMPATHETIC")
        
        # Transition vers DORSAL si effondrement imminent
        contexte_effondrement = {
            "niveau_menace": 0.3,
            "charge_systeme": 0.95,  # Surcharge critique
            "effondrement_detecte": True
        }
        transition = ventral.determiner_transition_necessaire(contexte_effondrement)
        self.assertEqual(transition, "DORSAL")


class TestArchitectureGuardianPredator(unittest.TestCase):
    """Tests pour l'architecture Guardian/Predator."""
    
    def setUp(self):
        """Configuration des tests."""
        self.systeme = SystemeResilience("TestSystem")
        self.evenements_test = [
            EvenementSysteme(
                timestamp=datetime.now(),
                type_evenement="maintenance_routine",
                severite="info",
                contexte={"routine": True},
                source="systeme_interne",
                impact_prevu=0.2
            )
        ]
    
    def test_systeme_resilience_initialisation(self):
        """Test de l'initialisation du système de résilience."""
        self.assertEqual(self.systeme.nom, "TestSystem")
        self.assertIsInstance(self.systeme.etat_actuel, EtatVentral)  # État initial
        self.assertIsNotNone(self.systeme.guardian)
        self.assertIsNotNone(self.systeme.predator)
    
    def test_orchestration_guardian_predator(self):
        """Test de l'orchestration Guardian/Predator."""
        resultat = self.systeme.orchestrer_resilience(self.evenements_test)
        
        # Vérification de la structure de réponse
        self.assertIn("etat_polyvagal", resultat)
        self.assertIn("intervention_guardian", resultat)
        self.assertIn("adaptation_predator", resultat)
        self.assertIn("metriques_souverainete", resultat)
        
        # Vérification que Guardian et Predator ont agi
        guardian_resultats = resultat["intervention_guardian"]["resultats"]
        predator_resultats = resultat["adaptation_predator"]["resultats"]
        
        self.assertIsInstance(guardian_resultats, dict)
        self.assertIsInstance(predator_resultats, dict)
    
    def test_evaluation_contexte_systemique(self):
        """Test de l'évaluation du contexte systémique."""
        contexte = self.systeme.evaluer_contexte_systemique(self.evenements_test)
        
        # Vérification des clés essentielles
        self.assertIn("timestamp", contexte)
        self.assertIn("nombre_evenements", contexte)
        self.assertIn("niveau_menace", contexte)
        self.assertIn("ressources_disponibles", contexte)
        self.assertIn("stabilite_systeme", contexte)
        
        # Vérification des valeurs cohérentes
        self.assertEqual(contexte["nombre_evenements"], len(self.evenements_test))
        self.assertGreaterEqual(contexte["niveau_menace"], 0.0)
        self.assertLessEqual(contexte["niveau_menace"], 1.0)


class TestConscienceSituationnelle(unittest.TestCase):
    """Tests pour la conscience situationnelle."""
    
    def setUp(self):
        """Configuration des tests."""
        self.conscience = ConscienceSituationnelle("TestConscience")
        self.signaux_test = [
            {
                "source": "capteur_test",
                "type": "performance",
                "amplitude": 0.7,
                "urgence": 0.3,
                "contexte": {"normal": True}
            }
        ]
    
    def test_perception_environnement(self):
        """Test de la perception de l'environnement."""
        perceptions = self.conscience.percevoir_environnement(self.signaux_test)
        
        self.assertIsInstance(perceptions, list)
        self.assertGreater(len(perceptions), 0)
        
        # Vérification de la structure des perceptions
        perception = perceptions[0]
        self.assertIsNotNone(perception.timestamp)
        self.assertIsNotNone(perception.source)
        self.assertIsNotNone(perception.intensite)
        self.assertIsNotNone(perception.fiabilite)
    
    def test_analyse_patterns_emergents(self):
        """Test de l'analyse des patterns émergents."""
        # Génération de perceptions d'abord
        self.conscience.percevoir_environnement(self.signaux_test)
        
        # Analyse des patterns
        patterns = self.conscience.analyser_patterns_emergents()
        
        self.assertIsInstance(patterns, list)
        # Les patterns peuvent être vides si pas assez de données
    
    def test_evaluation_contexte_global(self):
        """Test de l'évaluation du contexte global."""
        contexte = self.conscience.evaluer_contexte_global("VENTRAL")
        
        # Vérification des clés essentielles
        self.assertIn("niveau_conscience", contexte)
        self.assertIn("etat_polyvagal", contexte)
        self.assertIn("qualite_perception", contexte)
        self.assertIn("recommandations", contexte)
        
        # Vérification de la cohérence
        self.assertEqual(contexte["etat_polyvagal"], "VENTRAL")
        self.assertIsInstance(contexte["recommandations"], list)


class TestSouveraineteNumerique(unittest.TestCase):
    """Tests pour la souveraineté numérique."""
    
    def setUp(self):
        """Configuration des tests."""
        self.souverainete = SouveraineteNumerique("TestSouverainete")
        self.contexte_test = {
            "ressources_disponibles": 0.8,
            "stabilite_systeme": 0.9,
            "etat_polyvagal": "VENTRAL"
        }
    
    def test_initialisation_souverainete(self):
        """Test de l'initialisation de la souveraineté."""
        self.assertEqual(self.souverainete.nom, "TestSouverainete")
        self.assertEqual(self.souverainete.niveau_souverainete_global, NiveauSouverainete.AUTONOME)
        
        # Vérification que tous les domaines sont initialisés
        self.assertEqual(len(self.souverainete.metriques_domaines), len(DomaineSouverainete))
    
    def test_evaluation_souverainete_globale(self):
        """Test de l'évaluation globale de la souveraineté."""
        evaluation = self.souverainete.evaluer_souverainete_globale(self.contexte_test)
        
        # Vérification de la structure de réponse
        self.assertIn("niveau_global", evaluation)
        self.assertIn("classification", evaluation)
        self.assertIn("metriques_domaines", evaluation)
        self.assertIn("strategie_recommandee", evaluation)
        
        # Vérification des valeurs cohérentes
        self.assertGreaterEqual(evaluation["niveau_global"], 0.0)
        self.assertLessEqual(evaluation["niveau_global"], 1.0)
        self.assertIsInstance(evaluation["classification"], str)
    
    def test_analyse_dependances_critiques(self):
        """Test de l'analyse des dépendances critiques."""
        analyse = self.souverainete.analyser_dependances_critiques()
        
        # Vérification de la structure même sans dépendances
        self.assertIn("nombre_dependances_critiques", analyse)
        self.assertIn("analyse_par_domaine", analyse)
        self.assertIn("recommandations_reduction", analyse)
        
        self.assertIsInstance(analyse["recommandations_reduction"], list)
    
    def test_planification_renforcement(self):
        """Test de la planification du renforcement."""
        objectif = 0.9
        horizon = timedelta(days=90)
        
        plan = self.souverainete.planifier_renforcement_souverainete(objectif, horizon)
        
        # Vérification de la structure du plan
        self.assertIn("objectif_niveau", plan)
        self.assertIn("niveau_actuel", plan)
        self.assertIn("faisabilite", plan)
        
        self.assertEqual(plan["objectif_niveau"], objectif)


class TestIntegrationTPD(unittest.TestCase):
    """Tests d'intégration de l'architecture TPD complète."""
    
    def test_scenario_complet_stabilite(self):
        """Test d'un scénario complet en situation stable."""
        # Initialisation des composants
        systeme = SystemeResilience("IntegrationTest")
        conscience = ConscienceSituationnelle("IntegrationConscience")
        souverainete = SouveraineteNumerique("IntegrationSouverainete")
        
        # Événements bénins
        evenements = [
            EvenementSysteme(
                timestamp=datetime.now(),
                type_evenement="optimisation_performance",
                severite="info",
                contexte={"automatique": True},
                source="systeme_interne",
                impact_prevu=0.1
            )
        ]
        
        # Orchestration complète
        resultat_resilience = systeme.orchestrer_resilience(evenements)
        contexte_conscience = conscience.evaluer_contexte_global("VENTRAL")
        evaluation_souverainete = souverainete.evaluer_souverainete_globale({
            "ressources_disponibles": 0.9,
            "stabilite_systeme": 0.95,
            "etat_polyvagal": "VENTRAL"
        })
        
        # Vérifications d'intégration
        self.assertEqual(resultat_resilience["etat_polyvagal"], "VENTRAL")
        self.assertEqual(contexte_conscience["etat_polyvagal"], "VENTRAL")
        self.assertGreaterEqual(evaluation_souverainete["niveau_global"], 0.5)
        
        print(f"✅ Test d'intégration réussi:")
        print(f"   État: {resultat_resilience['etat_polyvagal']}")
        print(f"   Conscience: {contexte_conscience['niveau_conscience']}")
        print(f"   Souveraineté: {evaluation_souverainete['classification']}")


def run_tests():
    """Exécute tous les tests TPD avec rapport doctrinal."""
    print("🧠 TESTS DE VALIDATION TPD - THÉORIE POLYVAGALE DIGITALE")
    print("=" * 60)
    print("Validation de l'architecture neuro-inspirée selon la doctrine")
    print("Guardian/Predator | Tripartition: VENTRAL/SYMPATHETIC/DORSAL")
    print("=" * 60)
    
    # Configuration du test runner
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Ajout des classes de test
    test_classes = [
        TestEtatsPolyvagaux,
        TestArchitectureGuardianPredator, 
        TestConscienceSituationnelle,
        TestSouveraineteNumerique,
        TestIntegrationTPD
    ]
    
    for test_class in test_classes:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    
    # Exécution avec rapport détaillé
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Rapport final doctrinal
    print("\n" + "=" * 60)
    if result.wasSuccessful():
        print("🏆 VALIDATION TPD RÉUSSIE")
        print("✅ Architecture Guardian/Predator opérationnelle")
        print("✅ Tripartition polyvagale validée")
        print("✅ Conscience situationnelle fonctionnelle")
        print("✅ Souveraineté numérique implémentée")
        print("✅ Doctrine TPD respectée intégralement")
    else:
        print("❌ ÉCHECS DE VALIDATION DÉTECTÉS")
        print(f"Échecs: {len(result.failures)}")
        print(f"Erreurs: {len(result.errors)}")
        print("Révision nécessaire selon la doctrine TPD")
    
    print("=" * 60)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)