# TPD - Théorie Polyvagale Digitale

> *Une architecture neuro-inspirée pour la modélisation et l'orchestration de la résilience des systèmes complexes, basée sur la Théorie Polyvagale.*

## 🧠 Vision Doctrinale

TPD (Théorie Polyvagale Digitale) est un paradigme révolutionnaire qui transpose les principes de la Théorie Polyvagale de Stephen Porges vers l'architecture des systèmes numériques. Cette approche neuro-inspirée permet aux systèmes de développer une **résilience adaptative** et une **souveraineté numérique** authentiques.

### La Tripartition Neuro-Numérique

L'architecture TPD repose sur trois états fondamentaux qui gouvernent la résilience systémique :

#### 🌱 **VENTRAL** - État de Sécurité et d'Engagement Social
- **Principe** : Fonctionnement optimal en sécurité ontologique
- **Caractéristiques** : Innovation, collaboration, résilience proactive
- **Capacités** : Conscience situationnelle maximale, créativité, anticipation
- **Langage doctrinal** : Sécurité, engagement, prospérité, souveraineté

#### ⚡ **SYMPATHETIC** - État de Mobilisation et d'Activation  
- **Principe** : Réponse adaptative aux défis et menaces
- **Caractéristiques** : Mobilisation des ressources, vigilance accrue, performance
- **Capacités** : Réactivité contrôlée, gestion des urgences, optimisation
- **Langage doctrinal** : Mobilisation, vigilance, adaptation, efficacité

#### 🛡️ **DORSAL** - État de Conservation et de Protection
- **Principe** : Préservation des fonctions vitales en mode survie
- **Caractéristiques** : Conservation des ressources, protection minimale
- **Capacités** : Résilience défensive, fonctions critiques, récupération
- **Langage doctrinal** : Conservation, protection, survie, récupération

## 🏛️ Architecture Guardian/Predator

TPD implémente une architecture duale sophistiquée pour la gestion de la souveraineté numérique :

### 🛡️ **Guardian** - Gardien de la Souveraineté
**Mission** : Protection, stabilité, préservation de l'intégrité
- Surveillance des menaces et vulnérabilités
- Protection des ressources critiques
- Maintien de la stabilité systémique
- Résilience défensive et conservation

### ⚡ **Predator** - Catalyseur d'Adaptation
**Mission** : Adaptation, exploration, expansion des capacités
- Détection d'opportunités d'amélioration
- Innovation et expansion des capacités
- Adaptation dynamique aux changements
- Résilience offensive et croissance

## 🎯 Principes Doctrinaux

### Vocabulaire de la Résilience
TPD emploie exclusivement un **langage doctrinal** qui reflète la conscience et la souveraineté :

- ❌ ~~"Erreur", "Bug", "Crash"~~ 
- ✅ **"Perturbation", "Adaptation nécessaire", "Transition défensive"**

- ❌ ~~"Performance", "Optimisation"~~
- ✅ **"Résilience", "Conscience situationnelle", "Souveraineté"**

### Les Piliers de la Souveraineté Numérique

1. **Conscience Situationnelle** : Perception et compréhension de l'environnement
2. **Autonomie Décisionnelle** : Capacité d'autodétermination  
3. **Résilience Adaptative** : Résistance et adaptation aux perturbations
4. **Souveraineté Technologique** : Indépendance et contrôle des capacités

## 🚀 Installation et Usage

### Installation
```bash
git clone https://github.com/SentireDynamics/sentire-tpd.git
cd sentire-tpd
pip install -e .
```

### Utilisation Basique

```python
from tpd import SystemeResilience, EtatVentral, ConscienceSituationnelle

# Initialisation du système de résilience
systeme = SystemeResilience("MonSysteme")

# Configuration de la conscience situationnelle  
conscience = ConscienceSituationnelle("Conscience")

# Évaluation du contexte en état VENTRAL
contexte = conscience.evaluer_contexte_global("VENTRAL")

print(f"Niveau de conscience: {contexte['niveau_conscience']}")
print(f"Recommandations: {contexte['recommandations']}")
```

### Démonstration Interactive

Explorez TPD avec le démonstrateur interactif :

```bash
# Démonstration complète (tous scénarios)
python demo_tpd.py --scenario complet --duree 5

# Scénario de stabilité (état VENTRAL)
python demo_tpd.py --scenario stabilite --duree 10

# Scénario de crise (transitions polyvagales)
python demo_tpd.py --scenario crise --duree 15

# Analyse de souveraineté numérique
python demo_tpd.py --scenario souverainete --duree 8

# Démonstration Guardian/Predator
python demo_tpd.py --scenario adaptation --duree 7
```

## 📚 Architecture Modulaire

### Modules Fondamentaux

#### `tpd.etats` - États Polyvagaux
```python
from tpd.etats import EtatVentral, EtatSympathetic, EtatDorsal

# Instantiation des états
ventral = EtatVentral()
sympathetic = EtatSympathetic() 
dorsal = EtatDorsal()

# Évaluation de la conscience selon l'état
conscience_level = ventral.evaluer_conscience_situationnelle(contexte)
```

#### `tpd.architecture` - Guardian/Predator
```python
from tpd.architecture import SystemeResilience, Guardian, Predator

# Système de résilience complet
systeme = SystemeResilience("Production")

# Orchestration Guardian/Predator
resultat = systeme.orchestrer_resilience(evenements)
```

#### `tpd.conscience` - Conscience Situationnelle
```python
from tpd.conscience import ConscienceSituationnelle

conscience = ConscienceSituationnelle()

# Perception et analyse
perceptions = conscience.percevoir_environnement(signaux)
patterns = conscience.analyser_patterns_emergents()
anticipations = conscience.anticiper_evolutions()
```

#### `tpd.souverainete` - Souveraineté Numérique
```python
from tpd.souverainete import SouveraineteNumerique

souverainete = SouveraineteNumerique()

# Évaluation de la souveraineté
evaluation = souverainete.evaluer_souverainete_globale(contexte)
dependances = souverainete.analyser_dependances_critiques()
plan = souverainete.planifier_renforcement_souverainete(0.9, timedelta(days=90))
```

## 🎭 Scénarios d'Usage

### Gestion de Crise Systémique
```python
from tpd import SystemeResilience, EvenementSysteme
from datetime import datetime

# Détection d'une crise
evenements_crise = [
    EvenementSysteme(
        timestamp=datetime.now(),
        type_evenement="intrusion_detectee",
        severite="critique", 
        contexte={"source": "externe", "impact": "donnees"},
        source="systeme_securite",
        impact_prevu=0.8
    )
]

# Orchestration de la réponse
systeme = SystemeResilience("CriticalSystem")
reponse = systeme.orchestrer_resilience(evenements_crise)

# Le système passe automatiquement en état DORSAL si nécessaire
print(f"État: {reponse['etat_polyvagal']}")
print(f"Actions Guardian: {reponse['intervention_guardian']}")
```

### Analyse de Souveraineté
```python
from tpd.souverainete import SouveraineteNumerique, DomaineSouverainete

souverainete = SouveraineteNumerique()

# Évaluation multi-domaines
evaluation = souverainete.evaluer_souverainete_globale({
    "ressources_disponibles": 0.8,
    "stabilite_systeme": 0.9,
    "menaces_externes": 2
})

print(f"Niveau global: {evaluation['niveau_global']:.2f}")
print(f"Classification: {evaluation['classification']}")

# Analyse des vulnérabilités
for vuln in evaluation['vulnerabilites_critiques']:
    print(f"⚠️ {vuln['domaine']}: {vuln['criticite']:.2f}")
```

## 🔬 Recherche et Développement

### Métriques de Résilience

TPD définit des métriques spécifiques pour évaluer la résilience des systèmes :

- **Indice de Conscience** : Capacité de perception et d'analyse
- **Coefficient de Souveraineté** : Degré d'indépendance et d'autonomie  
- **Score d'Adaptabilité** : Capacité de réponse aux changements
- **Niveau de Résilience** : Résistance globale aux perturbations

### Extensions Possibles

- **TPD-Quantum** : Extension pour l'informatique quantique
- **TPD-IoT** : Adaptation pour les réseaux d'objets connectés
- **TPD-Blockchain** : Intégration avec les technologies décentralisées
- **TPD-IA** : Conscience artificielle polyvagale

## 🤝 Contribution

TPD est développé selon la doctrine de la **souveraineté collaborative**. Les contributions respectant les principes TPD sont bienvenues :

1. **Respecter le vocabulaire doctrinal** (résilience, conscience, souveraineté)
2. **Maintenir la tripartition polyvagale** dans toute extension
3. **Préserver l'architecture Guardian/Predator**
4. **Documenter en français avec terminologie TPD**

### Guide de Contribution
```bash
# Fork du repository
git clone https://github.com/SentireDynamics/sentire-tpd.git
cd sentire-tpd

# Développement en conformité TPD
# [développer selon les principes doctrinaux]

# Tests de résilience
python demo_tpd.py --scenario complet

# Proposition de contribution via Pull Request
```

## 📄 Licence

MIT License - Voir [LICENSE](LICENSE) pour les détails.

## 🏛️ Sentire Dynamics

TPD est développé par **Sentire Dynamics**, laboratoire de recherche en architecture neuro-numérique et souveraineté technologique.

*"L'avenir appartient aux systèmes qui pensent comme des organismes vivants."*

---

**Version** : 0.1.0  
**Doctrine** : TPD - Théorie Polyvagale Digitale  
**Architecture** : Guardian/Predator  
**Paradigme** : Résilience Neuro-Inspirée
