using Application.DTOs;
using Domain.Entities;
using Domain.Services;
using Microsoft.Extensions.Configuration;
using Newtonsoft.Json;
using System.Net.Http;
using System.Net.Http.Json;
using System.Threading.Tasks;

namespace Infrastructure.Services
{
    public class MedicationExternalService : IMedicationExternalService
    {
        private readonly HttpClient _httpClient;
        private readonly string? _apiKey;
        private readonly string? _baseUrl;

        public MedicationExternalService(HttpClient httpClient, IConfiguration configuration)
        {
            _httpClient = httpClient;
            _apiKey = configuration["ExternalApi:ApiKey"];
            _baseUrl = configuration["ExternalApi:BaseUrl"];
        }

        public async Task<List<ExternalMedication>> GetMedicationsByConditionAsync(string condition)
        {
            var request = new HttpRequestMessage(HttpMethod.Get, $"{_baseUrl}/medications/disease/{condition}");
            request.Headers.Add("Authorization", $"Bearer {_apiKey}"); // Sau un alt header, dacă API-ul extern necesită altceva

            var response = await _httpClient.SendAsync(request);
            if (!response.IsSuccessStatusCode)
            {
                return new List<ExternalMedication>(); // Poți trata mai bine erorile aici
            }

            var content = await response.Content.ReadAsStringAsync();
            return JsonConvert.DeserializeObject<List<ExternalMedication>>(content) ?? new List<ExternalMedication>();
        }
    }
}
