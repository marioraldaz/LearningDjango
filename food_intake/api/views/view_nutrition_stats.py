from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from food_intake.models import NutritionStats
from profiles.models import UserProfile  # Import UserProfile model (adjust path as needed)

class NutritionStatsView(DetailView):
    model = NutritionStats
    template_name = 'nutrition_stats_detail.html'  # Specify the template name

    def get_object(self, queryset=None):
        # Get the UserProfile ID from URL parameters
        profile_id = self.kwargs.get('profile_id')
        
        # Fetch the corresponding UserProfile instance or return 404 if not found
        profile = get_object_or_404(UserProfile, id=profile_id)

        # Retrieve NutritionStats instance related to the UserProfile
        nutrition_stats = NutritionStats.objects.filter(profile=profile).first()

        return nutrition_stats

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.object.profile  # Pass the UserProfile instance to context
        return context
