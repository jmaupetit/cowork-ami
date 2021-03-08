"""Models for the cowork app"""

import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Application(models.Model):
    """An application for the call for expression of interest"""

    class MondarverneCities(models.TextChoices):
        """Mondarverne communauté cities"""

        AUTHEZAT = "AUT", _("Authezat")
        AYDAT = "AYD", _("Aydat")
        BUSSEOL = "BUS", _("Busséol")
        CHANONAT = "CHA", _("Chanonat")
        CORENT = "COR", _("Corent")
        COURNOLS = "COU", _("Cournols")
        LAPS = "LAP", _("Laps")
        LA_ROCHE_BLANCHE = "LRB", _("La Roche-Blanche")
        LA_ROCHE_NOIRE = "LRN", _("La Roche-Noire")
        LA_SAUVETAT = "LSA", _("La Sauvetat")
        LES_MARTRES_DE_VEYRE = "LMV", _("Les Martres-de-Veyre")
        LE_CREST = "LCR", _("Le Crest")
        MANGLIEU = "MAN", _("Manglieu")
        MIREFLEURS = "MIR", _("Mirefleurs")
        OLLOIX = "OLL", _("Olloix")
        ORCET = "ORC", _("Orcet")
        PIGNOLS = "PIG", _("Pignols")
        SAINT_AMANT_TALLENDE = "SAT", _("Saint-Amant-Tallende")
        SAINT_GEORGES_SUR_ALLIER = "SGA", _("Saint-Georges-Sur-Allier")
        SAINT_MAURICE_ES_ALLIER = "SMA", _("Saint-Maurice-Sur-Allier")
        SAINT_SANDOUX = "SSD", _("Saint-Sandoux")
        SAINT_SATURNIN = "SST", _("Saint-Saturnin")
        SALLEDES = "SAL", _("Sallèdes")
        TALLENDE = "TAL", _("Tallende")
        VEYRE_MONTON = "VMT", _("Veyre-Monton")
        VIC_LE_COMTE = "VLC", _("Vic-Le-Comte")
        YRONDE_ET_BURON = "YEB", _("Yronde-et-Buron")

    class DesiredRoles(models.TextChoices):
        """Desired roles (implication)"""

        ASSOCIATE = "ASO", _("Membre fondateur")
        PERMANENT = "PMT", _("Résident (bureau permanent)")
        NOMAD = "NMD", _("Nomade (à la journée ou demi-journée)")
        WATCHER = "WAT", _("Sympatisant")

    class MonthlyBill(models.IntegerChoices):
        """Maximal monthly bill that a company can pay for"""

        STARTER = 1, _("moins de 100 euros")
        BRONZE = 2, _("entre 100 et 200 euros")
        SILVER = 3, _("entre 200 et 300 euros")
        GOLD = 4, _("plus de 300 euros")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    first_name = models.CharField(
        _("Prénom"),
        max_length=100,
        blank=False,
    )

    last_name = models.CharField(_("Nom"), max_length=100, blank=False)

    email = models.EmailField(_("Email"), unique=True, blank=False)

    city = models.CharField(
        _("Commune"),
        max_length=3,
        choices=MondarverneCities.choices,
        help_text=_("Indiquez la commune de votre résidence principale"),
    )

    desired_role = models.CharField(
        _("Role désiré"),
        max_length=3,
        choices=DesiredRoles.choices,
        help_text=_("Veuillez préciser votre niveau d'implication dans le projet"),
    )

    max_monthly_bill = models.IntegerField(
        _("Budget mensuel maximal"),
        choices=MonthlyBill.choices,
        help_text=_(
            "Veuillez indiquer quel montant maximal votre entreprise "
            "peut dépenser pour votre hébergement"
        ),
    )

    has_accepted_data_policy = models.BooleanField(
        _("J'accepte la potitique de gestion des données du présent questionnaire"),
        default=False,
    )

    has_validated_email = models.BooleanField(
        _("A validé son adresse email"), editable=False, default=False
    )

    class Meta:
        """Meta for the applications model"""

        ordering = ("last_name", "first_name")
        verbose_name = _("Candidature")
        verbose_name_plural = _("Candidatures")

    def __str__(self):
        """Get a string representation of applications"""
        return f"{self.last_name} {self.first_name} ({self.id})"
