import random
from django.core.management.base import BaseCommand
from django.db import transaction
from todos.models import Tache


TITRES = [
    "Apprendre les vues génériques Django",
    "Créer un modèle Tache",
    "Configurer les URLs",
    "Écrire les templates",
    "Tester le CRUD complet",
    "Comprendre ListView vs DetailView",
    "Maîtriser reverse_lazy",
    "Ajouter une pagination",
    "Implémenter une recherche",
    "Déployer sur un serveur",
    "Lire la documentation Django",
    "Réviser les migrations",
    "Ajouter du CSS au projet",
    "Créer une API REST",
    "Écrire des tests unitaires",
    "Utiliser les signaux Django",
    "Configurer l'admin",
    "Optimiser les requêtes ORM",
    "Explorer les formulaires Django",
    "Publier le projet sur GitHub",
]

DESCRIPTIONS = [
    "",
    "Prendre le temps de lire la doc officielle.",
    "Vérifier que tout fonctionne avec le serveur de dev.",
    "Ne pas oublier les migrations après le modèle.",
    "Tester sur mobile également.",
    "Important pour la suite du cours.",
    "À faire avant la prochaine séance.",
]


class Command(BaseCommand):
    help = "Peuple la base de données avec des tâches de démonstration"

    def add_arguments(self, parser):
        parser.add_argument(
            '--nombre', '-n',
            type=int,
            default=10,
            help="Nombre de tâches à créer (par défaut : 10)",
        )
        parser.add_argument(
            '--vider',
            action='store_true',
            help="Supprime toutes les tâches existantes avant de peupler",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        nombre = options['nombre']

        if options['vider']:
            total = Tache.objects.count()
            Tache.objects.all().delete()
            self.stdout.write(
                self.style.WARNING(f"🗑️  {total} tâche(s) supprimée(s).")
            )

        if nombre <= 0:
            self.stdout.write(self.style.WARNING("Aucune tâche à créer (nombre ≤ 0)."))
            return

        # On limite au nombre de titres disponibles
        nombre = min(nombre, len(TITRES))
        titres_choisis = random.sample(TITRES, nombre)

        taches_creees = []
        for i, titre in enumerate(titres_choisis, start=1):
            tache = Tache.objects.create(
                titre=titre,
                description=random.choice(DESCRIPTIONS),
                terminee=random.choice([True, False, False]),  # ~33% terminées
            )
            taches_creees.append(tache)
            self.stdout.write(f"  ✔ [{i}/{nombre}] {titre}")

        self.stdout.write(
            self.style.SUCCESS(
                f"\n🎉 {len(taches_creees)} tâche(s) créée(s) avec succès !"
            )
        )