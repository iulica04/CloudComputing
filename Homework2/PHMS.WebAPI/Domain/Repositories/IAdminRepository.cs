﻿using Domain.Common;
using Domain.Entities;

namespace Domain.Repositories
{
    public interface IAdminRepository
    {
        Task<IEnumerable<Admin>> GetAllAsync();
        Task<Admin?> GetByIdAsync(Guid id);
        Task UpdateAsync(Admin admin);
        Task DeleteAsync(Guid id);
        Task<Result<LoginResponse>> Login(string email, string password);

    }
}
