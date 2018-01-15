import datetime

from django.core.management.base import BaseCommand
from entity.models import Organization, OrganizationClassification
from government.models import Party


class Command(BaseCommand):
    help = (
        'Loads some political parties into database.'
    )

    def handle(self, *args, **options):
        print('Loading political parties')

        party, created = OrganizationClassification.objects.get_or_create(
            name="Political party")

        gop, created = Organization.objects.update_or_create(
            name="Republican Party",
            classification=party,
            defaults={
                'classification': party,
                'links': ['https://www.gop.com/'],
                'founding_date': datetime.date(1854, 3, 20),
            }
        )

        Party.objects.update_or_create(
            organization=gop,
            defaults={
                'label': 'Republican',
                'short_label': 'GOP',
                'ap_code': 'gop',
                'aggregate_candidates': False
            }
        )

        dem, created = Organization.objects.update_or_create(
            name="Democratic Party",
            defaults={
                'classification': party,
                'links': ['https://www.democrats.org/'],
                'founding_date': datetime.date(1828, 1, 8),
            }
        )

        Party.objects.update_or_create(
            organization=dem,
            defaults={
                'label': 'Democrat',
                'short_label': 'Dem',
                'ap_code': 'dem',
                'aggregate_candidates': False
            }
        )

        lib, created = Organization.objects.update_or_create(
            name="Libertarian Party",
            defaults={
                'classification': party,
                'links': ['http://www.lp.org/'],
                'founding_date': datetime.date(1971, 12, 11),
            }
        )

        Party.objects.update_or_create(
            organization=lib,
            defaults={
                'label': 'Libertarian',
                'short_label': 'Lib',
                'ap_code': 'lib',
            }
        )

        grn, created = Organization.objects.update_or_create(
            name="Green Party",
            defaults={
                'classification': party,
                'links': ['http://www.gp.org/'],
                'founding_date': datetime.date(2001, 4, 1),
            }
        )

        Party.objects.update_or_create(
            organization=grn,
            defaults={
                'label': 'Green',
                'short_label': 'Grn',
                'ap_code': 'grn',
            }
        )

        cst, created = Organization.objects.update_or_create(
            name="Constitution Party",
            defaults={
                'classification': party,
                'links': ['https://www.constitutionparty.com/'],
                'founding_date': datetime.date(1991, 1, 1),
            }
        )

        Party.objects.update_or_create(
            organization=cst,
            defaults={
                'label': 'Constitution Party',
                'short_label': 'Const.',
                'ap_code': 'cst',
            }
        )

        iap, created = Organization.objects.update_or_create(
            name="Independent American Party",
            defaults={
                'classification': party,
                'links': ['http://www.independentamericanparty.org/'],
                'founding_date': datetime.date(1998, 5, 16),
            }
        )

        Party.objects.update_or_create(
            organization=iap,
            defaults={
                'label': 'Independent American Party',
                'short_label': 'IAP',
                'ap_code': 'iap',
            }
        )

        Party.objects.update_or_create(
            label='Independent',
            defaults={
                'label': 'Independent',
                'short_label': 'Ind',
                'ap_code': 'ind',
            }
        )

        self.stdout.write(
            self.style.SUCCESS('Done.')
        )
